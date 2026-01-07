from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI(
    title="Movies Microservice",
    description="API za pregled filmskih podataka - RS6 Vježba",
    version="1.0.0"
)

# Uključivanje routera
app.include_router(filmovi_router)

@app.get("/")
def home():
    return {"message": "Dobrodošli na Movies API. Posjetite /docs za dokumentaciju."}

# Kod za pokretanje
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)