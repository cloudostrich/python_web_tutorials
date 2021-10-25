from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

basedir=os.path.dirname(os.path.realpath(__file__))
engine=create_engine("sqlite:///"+os.path.join(basedir,"pizza.db"), echo=True, future=True)

Base = declarative_base()


