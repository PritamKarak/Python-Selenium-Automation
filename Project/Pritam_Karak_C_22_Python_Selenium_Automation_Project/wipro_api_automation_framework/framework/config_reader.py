from pathlib import Path
import os
import yaml
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


def load_config():
    path = ROOT_DIR / "config" / "config.yaml"
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


CONFIG = load_config()


def get_setting(key, default=None):
    return os.getenv(key, default)


def get_timeout():
    return int(os.getenv("REQUEST_TIMEOUT", CONFIG["execution"]["timeout"]))


def verify_ssl():
    raw = os.getenv("VERIFY_SSL", str(CONFIG["execution"]["verify_ssl"]))
    return str(raw).lower() in {"1", "true", "yes", "y"}


def get_base_url(api_name):
    return CONFIG["apis"][api_name]["base_url"]
