from sqlmodel import SQLModel, create_engine
import os

basedir=os.path.dirname(os.path.realpath(__file__))
print(basedir)

conn_str = "sqlite:///"+os.path.join(basedir,"books.db")
print(conn_str)


engine=create_engine(conn_str,echo=True, future=True)
