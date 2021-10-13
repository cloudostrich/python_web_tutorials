from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Ariba'}}


@app.get('/blog')
def blog(cock=10, pub: bool = True, sort: Optional[str] = None):
    # limit to cock
    if pub:
        return {'responser':
                {'data': f'{cock} pubs from db',
                 'pub': f'pub_status={pub}',
                 'sort': sort}}
    else:
        return {'responser':
                {'data': f'All {cock} pubs',
                 'pub': f'pub_status={pub}',
                 'sort': sort}}


@app.get('/blog/{id}/comments')
def comments(id, limit: int = 10):
    # fetch comments with id=id, limit 10
    return {'data': {'1', '2'}, 'limit': limit}


@app.get('/{id}')
def about(id: int):
    return {'data': id}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': 'Blog is created', 'title': request.title, 'body': request.body, 'published': request.published_at}


if __name__ == "__main__":
    #    uvicorn.run('main:app', host='127.0.01', port=9000, log_level='info', reload=True) # reload for debugging
    uvicorn.run(app, host='127.0.01', port=9000, log_level='info')
