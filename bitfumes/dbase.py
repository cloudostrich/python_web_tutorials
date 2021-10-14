from sqlalchemy import create_engine  # 1st step
from sqlalchemy.ext.declarative import declarative_base  # 2nd step
from sqlalchemy.orm import sessionmaker, relationship  # 3rd step
from sqlalchemy import Column, Integer, String, ForeignKey  # for creating models

# Basic setup for sqlalchemy
DBurl = "sqlite:///./blog.db"
engine = create_engine(DBurl, connect_args={
                       "check_same_thread": False}, echo=True, future=True)

Base = declarative_base()

localsession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create model for tables


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="created_blogs")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_blogs = relationship("Blog", back_populates="creator")


#
