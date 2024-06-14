from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import products

templates = Jinja2Templates(directory="templates/")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# routers
app.include_router(products.router)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("task/index.html", context={"request": request})


@app.get("/app")
async def appme(request: Request):
    return templates.TemplateResponse("pro/index.html", context={"request": request})

# API endpoints

@app.get("/health")
async def health():
    return {"ping": "pong"}
