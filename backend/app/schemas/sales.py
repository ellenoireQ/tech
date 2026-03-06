from pydantic import BaseModel

# Data Penjualan Model
#
# example:
#
# DataPenjualan(
# product_name = "Produk A"
# jumlah_penjualan = 100
# harga = 50000
# diskon = 10
# status = "Laku"
# )
class DataPenjualan(BaseModel):
    product_name: str | None = None
    jumlah_penjualan: int
    harga: int
    diskon: int
    status: str | None = None


class PredictRequest(BaseModel):
    data: list[DataPenjualan]
