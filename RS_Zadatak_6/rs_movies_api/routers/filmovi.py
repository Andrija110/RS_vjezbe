import json
import os
from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Optional
from models import Movie, Actor, Writer
from pathlib import Path

router = APIRouter(prefix="/filmovi", tags=["filmovi"])

# In-memory baza podataka
movies_db: List[Movie] = []

# Funkcija za pretvaranje stringa imena u objekt
def parse_person(person_str: str) -> dict:
    parts = person_str.strip().split(" ")
    if len(parts) > 1:
        return {"name": parts[0], "surname": " ".join(parts[1:])}
    return {"name": parts[0], "surname": ""}

# Funkcija za učitavanje podataka pri pokretanju
def load_movies():
    file_path = Path(__file__).parent.parent / "data" / "movies.json"
    print(f"Učitavanje podataka iz {file_path}")
    if not file_path.exists():
        print(f"Upozorenje: Datoteka {file_path} ne postoji.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        
        for item in raw_data:
            # Parsiranje Actors i Writer iz stringova u liste objekata
            actors_list = []
            if "Actors" in item and isinstance(item["Actors"], str):
                names = item["Actors"].split(",")
                actors_list = [parse_person(n) for n in names if n.strip() != "N/A"]
            
            writers_list = []
            if "Writer" in item and isinstance(item["Writer"], str):
                names = item["Writer"].split(",")
                writers_list = [parse_person(n.split("(")[0]) for n in names if n.strip() != "N/A"]

            item["Actors"] = actors_list
            item["Writer"] = writers_list
            
            try:
                # Validacija kroz Pydantic model
                movie = Movie(**item)
                movies_db.append(movie)
            except Exception as e:
                print(f"Greška pri učitavanju filma {item.get('Title')}: {e}")

# Pozivamo učitavanje odmah pri importu modula
load_movies()

# --- RUTE ---

# Ruta za dohvaćanje svih filmova s filtriranjem
@router.get("/", response_model=List[Movie])
def get_all_movies(
    min_year: int = Query(default=None, ge=1900, description="Minimalna godina"),
    max_year: int = Query(default=None, ge=1900, description="Maksimalna godina"),
    min_rating: float = Query(default=None, ge=0, le=10, description="Minimalna ocjena"),
    max_rating: float = Query(default=None, ge=0, le=10, description="Maksimalna ocjena"),
    type: str = Query(default=None, regex="^(movie|series)$", description="Tip: movie ili series")
):
    filtered_movies = movies_db

    if min_year:
        filtered_movies = [m for m in filtered_movies if m.Year >= min_year]
    if max_year:
        filtered_movies = [m for m in filtered_movies if m.Year <= max_year]
    if min_rating:
        filtered_movies = [m for m in filtered_movies if (m.imdbRating or 0) >= min_rating]
    if max_rating:
        filtered_movies = [m for m in filtered_movies if (m.imdbRating or 0) <= max_rating]
    if type:
        filtered_movies = [m for m in filtered_movies if m.Type == type]

    return filtered_movies

# Ruta za dohvaćanje filma po imdbID
@router.get("/{imdb_id}", response_model=Movie)
def get_movie_by_id(imdb_id: str):
    for movie in movies_db:
        if movie.imdbID == imdb_id:
            return movie
    #Obrada greške ako ne postoji [cite: 1357]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Film s ID-em {imdb_id} nije pronađen"
    )

# Ruta za dohvaćanje filma po naslovu
@router.get("/naslov/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    for movie in movies_db:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Film s naslovom '{title}' nije pronađen"
    )