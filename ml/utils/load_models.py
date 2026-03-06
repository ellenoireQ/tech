import os
import joblib
import pandas as pd
from fastapi import HTTPException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_model(d: dict):
    model_path = os.path.join(BASE_DIR, "ml", "model.pkl")
    if not os.path.exists(model_path):
        raise HTTPException(status_code=503, detail="Model not found. Please train the model first.")
    model = joblib.load(model_path)
    df_input = pd.DataFrame(d["data"])
    df = df_input[["jumlah_penjualan", "harga", "diskon"]]
    result = model.predict(df)
    return result.tolist()
