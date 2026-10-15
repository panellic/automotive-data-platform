
from .config import MIN_MODEL_YEAR, MAX_MODEL_YEAR

REQUIRED_COLUMNS = [
    "vin",
    "brand",
    "model",
    "model_year",
    "engine_type",
    "country",
]

def validate_vehicles(df):
    
    missing_values = df.isnull().sum().sum()
    
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]
    
    duplicate_vins = df["vin"].duplicated().sum()
    
    invalid_model_years = (
        (df["model_year"] < MIN_MODEL_YEAR) |
        (df["model_year"] > MAX_MODEL_YEAR)
    ).sum()

    print("Missing values:", missing_values)
    
    print("Missing columns:", missing_columns)
    
    print("Duplicate VINs:", duplicate_vins)
    
    print("Invalid model years:", invalid_model_years)

    is_valid = (
        missing_values == 0
        and duplicate_vins == 0
        and invalid_model_years == 0
        and len(missing_columns) == 0
    )

    if is_valid:
        print("Validation PASSED")
    else:
        print("Validation FAILED")

    return bool(is_valid)
 