import pandas as pd

from src.validation import (
    validate_vehicles,
    count_missing_values,
    count_duplicate_vins,
    count_invalid_model_years,
    get_missing_columns,
)



def test_valid_vehicle_data():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", "VIN002"],
            "brand": ["Jeep", "Ram"],
            "model": ["Grand Cherokee", "1500"],
            "model_year": [2024, 2025],
            "engine_type": ["Gasoline", "Gasoline"],
            "country": ["USA", "USA"],
        }
    )

    assert validate_vehicles(df) is True
    

def test_duplicate_vin_fails_validation():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", "VIN001"],
            "brand": ["Jeep", "Jeep"],
            "model": ["Grand Cherokee", "Grand Cherokee"],
            "model_year": [2024, 2024],
            "engine_type": ["Gasoline", "Gasoline"],
            "country": ["USA", "USA"],
        }
    )

    assert validate_vehicles(df) is False
    
    
def test_invalid_model_year_fails_validation():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", "VIN002"],
            "brand": ["Jeep", "Ram"],
            "model": ["Grand Cherokee", "1500"],
            "model_year": [1995, 2025],
            "engine_type": ["Gasoline", "Gasoline"],
            "country": ["USA", "USA"],
        }
    )

    assert validate_vehicles(df) is False
    
    
def test_missing_vin_fails_validation():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", None],
            "brand": ["Jeep", "Ram"],
            "model": ["Grand Cherokee", "1500"],
            "model_year": [2024, 2025],
            "engine_type": ["Gasoline", "Gasoline"],
            "country": ["USA", "USA"],
        }
    )

    assert validate_vehicles(df) is False


from src.read_vehicles import load_vehicles

def test_missing_file_returns_none():
    df = load_vehicles("data/file_that_does_not_exist.csv")

    assert df is None
    
    
    
def test_missing_required_column_fails_validation():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", "VIN002"],
            "brand": ["Jeep", "Ram"],
            "model": ["Grand Cherokee", "1500"],
            "model_year": [2024, 2025],
            "engine_type": ["Gasoline", "Gasoline"],
        }
    )

    assert validate_vehicles(df) is False


def test_count_duplicate_vins():
    df = pd.DataFrame(
        {
            "vin": ["VIN001", "VIN001", "VIN002"],
        }
    )

    assert count_duplicate_vins(df) == 1