from typing import Union
from batch_prediction.prediction_service import PredictionService
from fastapi import FastAPI,Response
from fastapi.responses import HTMLResponse
import os
import pandas as pd

app = FastAPI()

@app.get("/")
async def model():
    message="<h1>Welcome to inferencing api</h1>"
    message2="<h2>Click on the below link to get the predictions</h2>"
    link="<a href='http://13.234.241.210:8000/predict'>Predict for Inferencing on batch data</a>"
    message=message+message2+link
    return HTMLResponse(content=message)
    

@app.get("/predict")
async def predict(response: Response):
    model_path =  f'{os.getcwd()}/artifacts/model/model.pkl'
    transformer_path = f'{os.getcwd()}/artifacts/features/transformer.pkl'
    batch_data = 'predict.tsv'
    prediction_service = PredictionService(model_path,transformer_path,batch_data)
    prediction_service.inference_batch()
    data=pd.read_csv("predict.csv")
    table_html = data.to_html(index=False)
    headers="<h1>Stack Overflow Data Inferncing on batch data</h1>"
    table_html = headers + table_html
    response.headers["Content-Type"] = "text/html"
    return HTMLResponse(content=table_html)

@app.get("/predict_single/{text}")
async def predict_single(text: str):
    model_path =  f'{os.getcwd()}/artifacts/model/model.pkl'
    transformer_path = f'{os.getcwd()}/artifacts/features/transformer.pkl'
    prediction_service = PredictionService(model_path,transformer_path)
    prediction = prediction_service.inference_single(text)
    return {"prediction": prediction}