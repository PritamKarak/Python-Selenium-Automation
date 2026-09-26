import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(tags=None):
    command = [sys.executable, "-m", "behave"]
    if tags:
        command.extend(["--tags", tags])
    print("Running:", " ".join(command))
    return subprocess.call(command, cwd=ROOT)


if __name__ == "__main__":
    tag = sys.argv[1] if len(sys.argv) > 1 else None
    raise SystemExit(run(tag))
