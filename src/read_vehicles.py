import pandas as pd

from .validation import validate_vehicles

def load_vehicles(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

df = load_vehicles("data/vehicles.csv")
#df = load_vehicles("data/vehicles_missing.csv")

if df is not None:
    print(df)

    is_valid = validate_vehicles(df)

    print("\nIs valid:", is_valid)


