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

usuarios = [{"name": "jose", "info": "some shit parks"},
            {"name": "fede", "info": "some fede shit"},
            {"name": "paula", "info": "some paula shit"}
            ]

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("task/index.html", context={"request": request, "usuarios": usuarios})


@app.get("/app")
async def appme(request: Request):
    return templates.TemplateResponse("pro/index.html", context={"request": request})

# API endpoints

@app.get("/health")
async def health():
    return {"ping": 200}

@app.post("/trigger_function")
def trigger_function(request: Request):
  # Call your function here
    result = clever_function()
    return templates.TemplateResponse("task/index.html", context={"request": request, "result": result, "usuarios": usuarios})
  
def clever_function():
    print("i did something")

templates.env.globals.update(clever_function=clever_function)