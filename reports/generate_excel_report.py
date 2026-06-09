import pandas as pd

def generate_excel_report(
    df,
    filename
):

    df.to_excel(
        filename,
        index=False
    )

    return filename