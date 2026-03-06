import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_model(d: dict):
    model = joblib.load(os.path.join(BASE_DIR, "ml", "model.pkl"))
    df_input = pd.DataFrame(d["data"])
    df = df_input[["jumlah_penjualan", "harga", "diskon"]]
    result = model.predict(df)
    return result.tolist()
