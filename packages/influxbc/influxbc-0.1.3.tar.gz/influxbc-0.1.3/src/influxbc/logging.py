import logging
import os

LOG_LEVEL = os.getenv("IBC_LOG_LEVEL", "WARNING")
LOGGER_NAME = "influxbc"

logger = logging.getLogger(LOGGER_NAME)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
