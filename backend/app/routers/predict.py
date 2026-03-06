from fastapi import APIRouter, HTTPException
from app.schemas.sales import PredictRequest

from ml.utils.load_models import load_model

router = APIRouter()


@router.post("", summary="Predict Sales Status", description="Predict whether each product will sell (Laris / Tidak Laris) based on sales features.")
def predict(request: PredictRequest):
    if not request.data:
        raise HTTPException(status_code=400, detail="data must not be empty")
    result = load_model(request.model_dump())
    return {"predictions": result}
