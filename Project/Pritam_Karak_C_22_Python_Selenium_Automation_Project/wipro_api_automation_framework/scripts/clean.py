from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

for name in ["allure-results", "allure-report"]:
    path = ROOT / name
    if path.exists():
        shutil.rmtree(path)

print("Cleaned Allure output directories.")
