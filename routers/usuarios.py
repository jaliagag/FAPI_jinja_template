from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", 
                   tags=["usuarios"], # para la documentacion
                   responses={ 404: { "message": "not found" } }
                   )


usuarios = [{"name": "jose2", "info": "some shit parks"},
            {"name": "fede2", "info": "some fede shit"},
            {"name": "paula2", "info": "some paula shit"}
            ]


@router.get("/")
async def get_users():
    return {"users": "users", "value": usuarios}

