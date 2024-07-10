from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import products, timer, usuarios
from routers.usuarios import get_users

templates = Jinja2Templates(directory="templates/")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# routers
# app.include_router(products.router)
app.include_router(timer.router)
app.include_router(usuarios.router)

# usuarios = [{"name": "jose", "info": "some shit parks"},
#             {"name": "fede", "info": "some fede shit"},
#             {"name": "paula", "info": "some paula shit"}
#             ]

@app.get("/")
async def index(request: Request):
    try:
        usuarios = await get_users()
        print("usuarios: ", usuarios)
        return templates.TemplateResponse("task/index.html", context={"request": request, "usuarios": usuarios})
    except Exception as e:
        return templates.TemplateResponse("task/index.html", context={"request": request})


# @app.get("/app")
# async def appme(request: Request):
#     return templates.TemplateResponse("pro/index.html", context={"request": request})

# API endpoints

@app.get("/health")
async def health():
    return {"ping": 200}
