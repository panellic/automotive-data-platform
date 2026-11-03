
import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

VEHICLES_FILE_PATH = BASE_DIR / "data" / "vehicles.csv"

MIN_MODEL_YEAR = 2000
MAX_MODEL_YEAR = 2030

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
