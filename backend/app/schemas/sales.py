from pydantic import BaseModel


class DataPenjualan(BaseModel):
    product_name: str | None = None
    jumlah_penjualan: int
    harga: int
    diskon: int
    status: str | None = None


class PredictRequest(BaseModel):
    data: list[DataPenjualan]
