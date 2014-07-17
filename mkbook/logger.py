import logging


def _get_logger():
    logger = logging.getLogger("mkbook")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug("create logger")
    return logger

logger = _get_logger()
