from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ml.utils.load_data import load_data

router = APIRouter()


@router.get("")
def sales():
    data = load_data()
    return JSONResponse(data)
