from fastapi import FastAPI, HTTPException
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from model import get_model, analyze_sentiment
from schemas import SentimentRequest
import uvicorn

app = FastAPI()

model = get_model()

@app.post("/analyze/", response_model=list)
def analyze_sentiment_endpoint(request: SentimentRequest):
    result = analyze_sentiment(request.text, model)
    return result

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"message": "Validation Error", "details": exc.errors()},
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# python fastapi_app.py;