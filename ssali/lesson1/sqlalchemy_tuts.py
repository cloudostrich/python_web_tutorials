#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlalchemy as sa


# In[22]:


from sqlalchemy.orm import declarative_base, sessionmaker


# In[3]:


from datetime import datetime


# In[10]:


import os


# In[5]:


sa.__version__


# ## Create schema of database, ie table schema

# In[6]:


Base = declarative_base()


# # User class/table
# class User
#     id int
#     username str
#     email str
#     date_created datetime
#     

# In[7]:


class User(Base):
    __tablename__='users'
    id=sa.Column(sa.Integer(), primary_key=True)
    username=sa.Column(sa.String(25),nullable=False, unique=True)
    email=sa.Column(sa.String(80), unique=True, nullable=False)
    date_created=sa.Column(sa.DateTime(),default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


# In[8]:


new_user = User(id=1, username="gugu", email="gugu@gugu.com")
print(new_user)


# ## set up pathname for db file, and create engine for dbase

# In[15]:


os.path.abspath('')


# In[16]:


#BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.abspath('')


# In[17]:


conn_str = "sqlite:///"+os.path.join(BASE_DIR,'site.db')


# In[ ]:





# In[18]:


engine = sa.create_engine(conn_str, echo=True)


# ### use User, engine and Base to create database

# In[19]:


# from main import User, engine, Base


# In[21]:


Base.metadata.create_all(engine)


# In[ ]:





# ## use sessionmaker to create session, to interact with dbase

# In[23]:


Session=sessionmaker()


# In[28]:


local_session=Session(bind=engine)


# In[30]:


new_user=User(username="ccb", email="ccb@cb.com")


# In[31]:


local_session.add(new_user)


# In[32]:


local_session.commit()


# In[33]:


users = [
    {"username":"knn",
    "email":"knn@knn.com"},
        {"username":"cok",
    "email":"cok@knn.com"},
        {"username":"lj",
    "email":"lj@knn.com"},
        {"username":"nabe",
    "email":"nabe@knn.com"},
]


# In[35]:


for u in users:
    new_user=User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    print(f"New User: {new_user} Added")

local_session.commit()


# ## Read data from dbase

# In[36]:


# from main import User, Session, engine


# In[37]:


#local_session=Session(bind=engine)


# In[39]:


# QUery for all
users=local_session.query(User).all()[:3]

for user in users:
    print(user.username)


# In[43]:


# Query for 1 row 
#oneguy = local_session.query(User).filter(User.username=='ccb').first()
oneguy = local_session.query(User).filter(User.username=='ccb').all()

print(oneguy)


# In[41]:


oneguy = local_session.query(User).first()
print(oneguy)


# ### Update a row

# In[44]:


user_2_update = local_session.query(User).filter(User.username=='ccb').first()

user_2_update.username = 'knnccb'
user_2_update.email = 'knnccb@ccb.com'

local_session.commit()


# ## Delete a record

# In[45]:


user2del = local_session.query(User).filter(User.username=='cok').first()

local_session.delete(user2del)
local_session.commit()


# ## Ordering results of query

# In[46]:


# Ascending
users = local_session.query(User).order_by(User.username).all()
print(users)


# In[48]:


for user in users:
    print(user.username)


# In[49]:


# Descending
users_desc = local_session.query(User).order_by(sa.desc(User.username)).all()

for user in users_desc:
    print(user.username)


# In[ ]:




