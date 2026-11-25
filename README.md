# ML FastAPI Docker

Классификация ирисов (Iris, RandomForest), развёрнутая как API на FastAPI и упакованная в Docker.

## Структура
- train.py - обучает модель и сохраняет model.joblib
- main.py - FastAPI-приложение (GET / и POST /predict)
- Dockerfile - инструкция для контейнера

## Локальный запуск
pip install -r requirements.txt
python train.py
uvicorn main:app --reload

Swagger: http://127.0.0.1:8000/docs

## Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api

## Пример запроса
POST /predict
{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}

Ответ: {"prediction": 0, "class_name": "setosa"}
