import os
import joblib

from ml.utils.load_data import load_data
from ml.utils.train import train_model


def test_train_produces_model_pkl(ml_dir, monkeypatch):
    monkeypatch.chdir(ml_dir)

    data = load_data(20)
    train_model(data)

    model_path = os.path.join(ml_dir, "model.pkl")
    assert os.path.exists(model_path), "model.pkl is not created"

    model = joblib.load(model_path)
    assert hasattr(model, "predict"), "model.pkl is not a valid sklearn model"
