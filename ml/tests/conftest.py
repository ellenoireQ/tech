import os
import pytest

ML_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def ml_dir():
    return ML_DIR
