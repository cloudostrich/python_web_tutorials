from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from models import Book
from database import engine
from sqlmodel import Session, select
from typing import Optional, List


app=FastAPI()

sessionlocal = Session(bind=engine)

@app.get('/books', response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    statement=select(Book)
    result=sessionlocal.exec(statement).all()
    return result


@app.post('/books', response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_a_book(book:Book):
    new_book=Book(title=book.title, description=book.description)
    sessionlocal.add(new_book)
    sessionlocal.commit()
    return new_book


@app.get('/book/{book_id}', response_model=Book)
async def get_all_books(book_id:int):
    statement=select(Book).where(Book.id==book_id)
    result = sessionlocal.exec(statement).first()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Yo yo, aint got it bro")
    return result



@app.put('/book/{book_id}')
async def get_all_books(book_id:int,book:Book):
    statement=select(Book).where(Book.id==book_id)
    result=sessionlocal.exec(statement).first()
    result.title=book.title
    result.description=book.description
    sessionlocal.commit()
    return result

@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    statement=select(Book).where(Book.id==book_id)
    result=sessionlocal.exec(statement).one_or_none()
    if result==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find lah")
    sessionlocal.delete(result)
    sessionlocal.commit()
    return result
