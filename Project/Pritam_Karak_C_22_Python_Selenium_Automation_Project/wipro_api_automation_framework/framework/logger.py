import logging
from pathlib import Path
from framework.config_reader import ROOT_DIR, CONFIG

LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "api_automation.log"

logger = logging.getLogger("api_automation")
logger.setLevel(getattr(logging, CONFIG["execution"].get("log_level", "INFO").upper(), logging.INFO))

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
