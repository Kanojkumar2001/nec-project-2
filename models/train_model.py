import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from models.model_evaluation import evaluate

MODEL_PATH = "models/sales_forecast_model.pkl"


def train_model(df):

    X = df[["year", "month", "day", "quantity"]]

    y = df["total_sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = evaluate(y_test, predictions)

    joblib.dump(model, MODEL_PATH)

    return {
        "r2": metrics["R2"],
        "mae": metrics["MAE"],
        "mse": metrics["MSE"],
        "predictions": predictions.tolist(),
        "actual": y_test.tolist(),
        "feature_importance": dict(
            zip(
                ["year", "month", "day", "quantity"],
                model.feature_importances_.tolist()
            )
        )
    }