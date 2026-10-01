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