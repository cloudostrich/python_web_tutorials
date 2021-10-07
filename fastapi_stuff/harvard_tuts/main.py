from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/jstuff")
async def read_item(request: Request):
    return templates.TemplateResponse("jstuff.html", {"request": request})

@app.get("/tasks")
async def read_item(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request})

@app.get("/single")
async def read_item(request: Request):
    return templates.TemplateResponse("singlepage.html", {"request": request})

@app.get("/scroll")
async def read_item(request: Request):
    return templates.TemplateResponse("scroll.html", {"request": request})

@app.get("/animate")
async def read_item(request: Request):
    return templates.TemplateResponse("animate.html", {"request": request})