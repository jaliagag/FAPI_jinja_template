from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(prefix="/usuarios", 
                   tags=["usuarios"], # para la documentacion
                   responses={ 404: { "message": "not found" } }
                   )

class Usuario(BaseModel):
    name: str | None = None
    info: str | None = None

usuarios = [{"name": "jose2", "info": "some ASDFASDFshit parks"},
            {"name": "fede2", "info": "some fede shitASDFADSF"},
            {"name": "paula2", "info": "some paula shit"},
            {"name": "fede2", "info": "some fede shitASDFADSF"},
            {"name": "asdf", "info": "some shit"}
            ]


@router.get("/")
async def get_users():
    return usuarios

@router.post("/", status_code=201, response_model=Usuario)
async def update_users(user: Usuario):
    update_user_encoded = jsonable_encoder(user)
    usuarios.append(update_user_encoded)
    return update_user_encoded

@router.delete("/{id}")
async def delete_user(id: str):
    del usuarios[int(id)]
    return "user deleted"