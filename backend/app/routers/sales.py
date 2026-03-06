from fastapi import APIRouter, HTTPException
from ml.utils.load_data import load_data

router = APIRouter()


@router.get("", summary="Get Sales Data", description="Return sales data. Use `expand` to set how many records to return (default: 10).")
def sales(expand: int = 10):
    if expand < 1:
        raise HTTPException(status_code=400, detail="expand must be greater than 0")
    data = load_data(expand)
    return data
