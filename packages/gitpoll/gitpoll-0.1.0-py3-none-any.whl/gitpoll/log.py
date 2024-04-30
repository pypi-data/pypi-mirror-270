# gitpoll/log.py
import logging
import sys
from logging.handlers import RotatingFileHandler
from .config import LOGGING_LOCATION, LOGGER_NAME, MAX_LOG_SIZE, MAX_LOG_FILES


def get_logger() -> logging.Logger:
    """Configure and retrieve a logger instance for the application."""
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )

    file_handler = RotatingFileHandler(
        LOGGING_LOCATION, maxBytes=MAX_LOG_SIZE, backupCount=MAX_LOG_FILES
    )
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


logger = get_logger()
