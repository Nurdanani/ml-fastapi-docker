import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Iris ML API")

artifact = joblib.load("model.joblib")
model = artifact["model"]
target_names = artifact["target_names"]


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def root():
    return {"message": "ML API is running"}


@app.post("/predict")
def predict(features: IrisFeatures):
    x = [[features.sepal_length, features.sepal_width,
          features.petal_length, features.petal_width]]
    pred = int(model.predict(x)[0])
    return {"prediction": pred, "class_name": target_names[pred]}