import logging
import sys

from data import config
from loguru import logger


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG",
    }

    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(self._get_level(record), record.getMessage())


def setup():
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
    )
    logger.add(config.LOGS_BASE_PATH + "/out.log", retention="1 day")
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
