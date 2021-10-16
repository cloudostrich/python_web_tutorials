from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import dbase, schemas

router = APIRouter()


# just to demo response_model in list
@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def allblogs2(db: Session = Depends(dbase.get_db)):
    blogs = db.query(dbase.Blog).all()
    return blogs

#
