from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ml.utils.load_data import load_data

router = APIRouter()

# Sales Data Endpoint
# method: GET
# description: Returns sales data in JSON format. Accepts an optional query parameter 'expand' to specify how many records to return (default is 10).
#
# example (cUrl):
# curl -X GET "http://localhost:8000/sales?expand=20"
#
@router.get("")
def sales(expand: int = 10):
    data = load_data(expand)
    return data
