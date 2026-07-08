import pandas as pd


def load_excel(filepath, sheet_name=0):
    """Load an Excel file into a pandas DataFrame."""
    df = pd.read_excel(filepath, sheet_name=sheet_name, engine="openpyxl")
    return df


def save_excel(df, filepath):
    """Save a pandas DataFrame to an Excel file."""
    df.to_excel(filepath, index=False, engine="openpyxl")
