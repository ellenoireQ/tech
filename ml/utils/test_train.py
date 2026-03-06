import os
import joblib
import pytest

from ml.utils.load_data import load_data
from ml.utils.train import train_model

ML_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Test to ensure that the train_model function creates a model.pkl file and that it is a valid sklearn model.
def test_train_produces_model_pkl(monkeypatch):
    monkeypatch.chdir(ML_DIR)

    data = load_data(20)
    train_model(data)

    model_path = os.path.join(ML_DIR, "model.pkl")
    assert os.path.exists(model_path), "model.pkl is not created"

    model = joblib.load(model_path)
    assert hasattr(model, "predict"), "model.pkl is not a valid sklearn model"
