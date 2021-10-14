from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str
    

class Blog(BlogBase):
    class Config():
        orm_mode = True
        
        
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    created_blogs: List[Blog]=[]
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):   # if inherit Blog, no need to put titile, body
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
