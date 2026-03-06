from backend.app.schemas.sales import PredictRequest
from fastapi import APIRouter
from pydantic import BaseModel

from ml.utils.load_models import load_model

router = APIRouter()

# Prediction Endpoint
# method: POST
# description: Accepts JSON input, runs the ML model, and returns predictions.
#
# example (cUrl):
# curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" 
# -d '{"data": [{"feature1": 10, "feature2": 20, "feature3": 30}]}'
#
@router.post("")
def predict(request: PredictRequest):
    result = load_model(request.model_dump())
    return {"predictions": result}
