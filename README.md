# ML FastAPI Docker

Классификация ирисов (Iris, RandomForest), развёрнутая как API на FastAPI и упакованная в Docker.

## Структура

* train.py - обучает модель и сохраняет model.joblib
* main.py - FastAPI-приложение (GET / и POST /predict)
* Dockerfile - инструкция для контейнера

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
{"sepal\_length": 5.1, "sepal\_width": 3.5, "petal\_length": 1.4, "petal\_width": 0.2}

Ответ: {"prediction": 0, "class\_name": "setosa"}

## MLflow

pip install -r requirements-mlflow.txt

python train\_mlflow.py

mlflow ui --backend-store-uri sqlite:///mlflow.db



Эксперимент: iris-classification. Логируются параметры (n\_estimators, max\_depth,

random\_state), метрики (accuracy, f1\_score) и артефакт model.joblib.

Модель зарегистрирована в Model Registry: iris-rf-model, version 1.



\## Streamlit

Сначала запустите API (docker run -p 8000:8000 ml-api), затем:

streamlit run streamlit\_app.py

Интерфейс: http://localhost:8501



\## Скриншоты

См. папку C:\\Users\\acer\\Desktop\\screenshots\_ml

