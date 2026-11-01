from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
CACHE_DIR = PROJECT_ROOT / "cache_fastf1"

for path in (DATA_RAW, DATA_PROCESSED, CACHE_DIR):
    path.mkdir(parents=True, exist_ok=True)
