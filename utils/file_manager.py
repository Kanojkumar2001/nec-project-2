import os

def create_project_folders():

    folders = [

        "outputs",

        "outputs/reports",

        "outputs/charts",

        "outputs/predictions"
    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )