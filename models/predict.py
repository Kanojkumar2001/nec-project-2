import joblib
import pandas as pd

MODEL_PATH = "models/sales_forecast_model.pkl"

def predict_sales(data):

    model = joblib.load(MODEL_PATH)

    prediction = model.predict(data)

    return prediction