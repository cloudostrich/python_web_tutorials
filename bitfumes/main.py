from fastapi import FastAPI, Depends, status, Response, HTTPException
# from pydantic import BaseModel # transferred to schemas
import schemas
import dbase
from sqlalchemy.orm import Session


app = FastAPI()


# class Blog(BaseModel):
#    title: str
#    body: str

dbase.Base.metadata.create_all(dbase.engine)


def get_db():
    db = dbase.localsession()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = dbase.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def getblogs(db: Session = Depends(get_db)):
    blogs = db.query(dbase.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id).first()
    if not blog:
        #        response.status_code = status.HTTP_404_NOT_FOUND
        #        return {'message': f"Dun have id {id} lah"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Dun have id {id} lah")
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(dbase.Blog).filter(dbase.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog id {id} not found")

    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'

#
