# utils/logger.py

import logging
import os

def get_logger(name=__name__):
    log_path = os.path.join("Logs", "test.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
