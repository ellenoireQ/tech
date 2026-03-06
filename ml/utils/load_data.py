import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# load_data
#
# Description:
# Loads data from the sales_data.csv file and returns it in JSON format.
# Once loaded, the data can be used for prediction.
#
# example;
# load_data(10): meaning is expanding value 10
#
def load_data(expand: int):
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

    return {"data": sales_data.head(expand).to_dict(orient="records")}
