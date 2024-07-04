from fastapi import APIRouter
import datetime

router = APIRouter(prefix="/timer", 
                   tags=["timer"], # para la documentacion
                   responses={ 404: { "message": "not found" } }
                   )


@router.get("/")
async def timer():
    now = datetime.datetime.now()
    return {"time": "time", "value": now.time()}

