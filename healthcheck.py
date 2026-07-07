import sys

print("=== Bitcoin Guardian Health Check ===\n")

print(f"Python Version: {sys.version}\n")

packages = [
    "yfinance",
    "pandas",
    "numpy",
    "requests",
    "ta",
    "rich",
    "sqlalchemy",
    "dotenv",
]

for package in packages:
    try:
        __import__(package)
        print(f"✅ {package}")
    except ImportError:
        print(f"❌ {package}")

print("\nHealth check complete.")