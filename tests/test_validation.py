import pandas as pd

from src.validation import validate_vehicles


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