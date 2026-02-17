# utils/logger.py
import logging
import os
import sys

LOG_DIR = "artifacts/logs"
LOG_FILE = os.path.join(LOG_DIR, "run.log")


def get_logger(name: str) -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # IMPORTANT: don't pass logs to root (prevents duplicates)
    logger.propagate = False

    # prevent duplicate handlers when pytest imports many times
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # 1) Console handler -> force stdout so you see it in terminal
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    # 2) File handler
    fh = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


# Optional: keep this so `from utils.logger import setup_logging` works
def setup_logging() -> logging.Logger:
    return get_logger("root")