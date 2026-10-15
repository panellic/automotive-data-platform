
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

VEHICLES_FILE_PATH = BASE_DIR / "data" / "vehicles.csv"

MIN_MODEL_YEAR = 2000
MAX_MODEL_YEAR = 2030