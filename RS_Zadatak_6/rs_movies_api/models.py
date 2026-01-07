from pydantic import BaseModel, Field, field_validator, ValidationInfo
from typing import List, Optional, Literal

# Modeli za glumce i pisce
class Actor(BaseModel):
    name: str
    surname: str

class Writer(BaseModel):
    name: str
    surname: str

# Glavni model filma
class Movie(BaseModel):
    Title: str
    Year: int = Field(..., ge=1900, description="Godina mora biti veća od 1900")
    Rated: str
    Runtime: int = Field(..., gt=0, description="Trajanje u minutama mora biti veće od 0")
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor] 
    Writer: List[Writer]
    Plot: str
    
    Type: Literal["movie", "series"]
    Images: List[str] = Field(default_factory=list) # Lista javnih poveznica
    
    # Validacija ocjena
    imdbRating: Optional[float] = Field(None, ge=0, le=10)
    imdbVotes: Optional[int] = Field(None, gt=0)
    
    # Identifikator
    imdbID: str

    # Ostali neobavezni atributi s default vrijednostima
    Released: Optional[str] = "N/A"
    Director: Optional[str] = "N/A"
    Awards: Optional[str] = "N/A"
    Poster: Optional[str] = None
    Metascore: Optional[str] = "N/A"
    
    @field_validator('Year', mode='before')
    @classmethod
    def parse_year(cls, v):
        if isinstance(v, str):
            clean_v = ''.join(filter(str.isdigit, v))[:4]
            return int(clean_v) if clean_v else 0
        return v

    @field_validator('Runtime', mode='before')
    @classmethod
    def parse_runtime(cls, v):
        if isinstance(v, str):
            clean_v = ''.join(filter(str.isdigit, v))
            return int(clean_v) if clean_v else 0
        return v

    @field_validator('imdbRating', mode='before')
    @classmethod
    def parse_rating(cls, v):
        if isinstance(v, str):
            try:
                return float(v)
            except ValueError:
                return None
        return v

    @field_validator('imdbVotes', mode='before')
    @classmethod
    def parse_votes(cls, v):
        if isinstance(v, str):
            clean_v = v.replace(",", "")
            try:
                return int(clean_v)
            except ValueError:
                return None
        return v