import joblib

MODEL_PATH = "models/sales_forecast_model.pkl"

def load_model():

    model = joblib.load(MODEL_PATH)

    return model