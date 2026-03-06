import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_data():
    cols = [
        "product_id",
        "product_name",
        "jumlah_penjualan",
        "harga",
        "diskon",
        "status",
    ]

    sales_data = pd.read_csv(
        os.path.join(BASE_DIR, "data", "sales_data.csv"),
        index_col="product_id",
        usecols=cols,
    )

    return sales_data.to_dict(orient="records")
