from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ml.utils.load_data import load_data

router = APIRouter()


@router.get("")
def sales(expand: int = 10):
    data = load_data(expand)
    return data
