import joblib
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

# Хранилище MLflow: локальная база SQLite (нужна для Model Registry)
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("iris-classification")

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}

with mlflow.start_run(run_name="random_forest"):
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")

    # Логируем параметры и метрики
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Сохраняем файл модели для API и логируем его как артефакт
    joblib.dump(
        {"model": model, "target_names": list(iris.target_names)},
        "model.joblib",
    )
    mlflow.log_artifact("model.joblib")

    # Логируем модель и регистрируем её в Model Registry
    mlflow.sklearn.log_model(
        model,
        name="model",
        registered_model_name="iris-rf-model",
        skops_trusted_types=["sklearn.tree._tree.Tree"],
    )

    print("Accuracy:", acc)
    print("F1-score:", f1)