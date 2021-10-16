from fastapi import FastAPI, Depends, status, Response, HTTPException
# from pydantic import BaseModel # transferred to schemas
import schemas
import hashing
import dbase
from sqlalchemy.orm import Session
from typing import List
from routers import blog


app = FastAPI()


# class Blog(BaseModel):
#    title: str
#    body: str

dbase.Base.metadata.create_all(dbase.engine)

# router stuff
app.include_router(blog.router)

# def get_db():
#    db = dbase.localsession()
#    try:
#        yield db
#    finally:
#        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(dbase.get_db)):
    # TODO: paramiz user_id
    new_blog = dbase.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# just to demo response_model in list
# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def allblogs2(db: Session = Depends(dbase.get_db)):
#    blogs = db.query(dbase.Blog).all()
#    return blogs


# @app.get('/blog')
# def getblogs(db: Session = Depends(dbase.get_db)):
#    blogs = db.query(dbase.Blog).all()
#    return blogs


@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, response: Response, db: Session = Depends(dbase.get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id).first()
    if not blog:
        #        response.status_code = status.HTTP_404_NOT_FOUND
        #        return {'message': f"Dun have id {id} lah"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Dun have id {id} lah")
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db: Session = Depends(dbase.get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(dbase.get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog id {id} not found")

    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(dbase.get_db)):
    new_user = dbase.User(
        name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user', response_model=schemas.ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(dbase.get_db)):
    user = db.query(dbase.User).filter(dbase.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is no user with id {id}")
    return user
#
