from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vibe Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
   allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Backend is running"}