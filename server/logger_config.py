# server/logger_config.py
import logging
import os
from datetime import datetime

def setup_logger():
    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger('WebServer')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler('logs/server.log')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
