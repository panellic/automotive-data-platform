
import pandas as pd

from .config import VEHICLES_FILE_PATH

from .validation import validate_vehicles

def load_vehicles(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

df = load_vehicles(VEHICLES_FILE_PATH)

if df is not None:
    print(df)

    is_valid = validate_vehicles(df)

    print("\nIs valid:", is_valid)


if __name__ == "__main__":
    df = load_vehicles("data/vehicles.csv")

    if df is not None:
        print(df)

        is_valid = validate_vehicles(df)

        print("\nIs valid:", is_valid)
        
        