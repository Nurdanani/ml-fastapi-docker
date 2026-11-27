\# ML FastAPI Docker



Классификация ирисов (датасет Iris, RandomForest), развёрнутая как API на FastAPI и упакованная в Docker. Дополнительно: отслеживание экспериментов в MLflow и интерфейс на Streamlit.



\## Структура проекта



\- `train.py` - обучает модель и сохраняет `model.joblib`

\- `main.py` - FastAPI-приложение (`GET /` и `POST /predict`)

\- `Dockerfile` - инструкция для контейнера

\- `train_mlflow.py` - обучение с логированием в MLflow и регистрацией модели

\- `streamlit_app.py` - веб-интерфейс на Streamlit

\- `requirements.txt` - зависимости API

\- `requirements-mlflow.txt` - зависимости MLflow и Streamlit



\## Локальный запуск API



```bash

pip install -r requirements.txt

python train.py

uvicorn main:app --reload

```



Swagger: http://127.0.0.1:8000/docs



\## Docker



```bash

docker build -t ml-api .

docker run -p 8000:8000 ml-api

```



\## Пример запроса



`POST /predict`



```json

{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}

```



Ответ:



```json

{"prediction": 0, "class_name": "setosa"}

```



\## MLflow



```bash

pip install -r requirements-mlflow.txt

python train_mlflow.py

mlflow ui --backend-store-uri sqlite:///mlflow.db

```



Интерфейс MLflow: http://127.0.0.1:5000



\- Эксперимент: `iris-classification`

\- Параметры: `n_estimators`, `max_depth`, `random_state`

\- Метрики: `accuracy`, `f1_score`

\- Артефакт: `model.joblib`

\- Model Registry: модель `iris-rf-model`, версия 1



\## Streamlit



Сначала запустите API (`docker run -p 8000:8000 ml-api`), затем:



```bash

streamlit run streamlit_app.py

```



Интерфейс: http://localhost:8501



\## Скриншоты



Скриншоты MLflow (запуск, метрики, артефакты, Model Registry) и интерфейса Streamlit находятся в папке \[screenshots](screenshots/).


