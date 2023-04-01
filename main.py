from typing import Union
from batch_prediction.prediction_service import PredictionService
from fastapi import FastAPI,Response
from fastapi.responses import HTMLResponse
import os
import pandas as pd

app = FastAPI()

@app.get("/")
async def model():
    return {"message":"This is model inferencing api"}

@app.get("/predict")
async def predict(response: Response):
    model_path =  f'{os.getcwd()}/artifacts/model/model.pkl'
    transformer_path = f'{os.getcwd()}/artifacts/features/transformer.pkl'
    batch_data = 'predict.tsv'
    prediction_service = PredictionService(model_path,transformer_path,batch_data)
    prediction_service.inference()
    data=pd.read_csv("predict.csv")
    table_html = data.to_html(index=False)
    response.headers["Content-Type"] = "text/html"
    return HTMLResponse(content=table_html)