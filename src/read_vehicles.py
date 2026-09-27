import pandas as pd

from validation import validate_vehicles

def load_vehicles(file_path):
    df = pd.read_csv(file_path)
    return df

df = load_vehicles("data/vehicles.csv")

print(df)

is_valid = validate_vehicles(df)

print("\nIs valid:", is_valid)


