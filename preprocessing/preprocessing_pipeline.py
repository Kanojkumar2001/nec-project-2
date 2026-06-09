from preprocessing.data_cleaning import clean_data
from preprocessing.feature_engineering import create_features
from preprocessing.outlier_handler import remove_outliers

def run_pipeline(df):

    df = clean_data(df)

    df = create_features(df)

    df = remove_outliers(df)

    return df