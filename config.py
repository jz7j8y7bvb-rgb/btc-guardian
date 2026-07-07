from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

APP_NAME = "Bitcoin Guardian"
VERSION = "1.0.0-alpha"

DATABASE_FILE = BASE_DIR / "data" / "guardian.db"

LOG_DIR = BASE_DIR / "logs"

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")