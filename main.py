# src/main.py

from fastapi import FastAPI

from src.router import book_router

app = FastAPI()

app.include_router(book_router)
__all__ = ["app"]
