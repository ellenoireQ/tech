from fastapi import APIRouter
from pydantic import BaseModel

from ml.utils.load_models import load_model

router = APIRouter()


class DataPenjualan(BaseModel):
    product_name: str | None = None
    jumlah_penjualan: int
    harga: int
    diskon: int
    status: str | None = None


class PredictRequest(BaseModel):
    data: list[DataPenjualan]


@router.post("")
def predict(request: PredictRequest):
    result = load_model(request.model_dump())
    return {"predictions": result}
