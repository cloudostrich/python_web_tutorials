from sqlmodel import SQLModel
from models import Book
from database import engine

print("Creating Database.....")

SQLModel.metadata.create_all(engine)

