from sqlmodel import SQLModel, Field
from typing import Optional


# model is for both sql table and pydantic model, so need table=true
class Book(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    title:str
    description:str
