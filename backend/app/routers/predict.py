from backend.app.schemas.sales import PredictRequest
from fastapi import APIRouter
from pydantic import BaseModel

from ml.utils.load_models import load_model

router = APIRouter()

@router.post("")
def predict(request: PredictRequest):
    result = load_model(request.model_dump())
    return {"predictions": result}
