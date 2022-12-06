import logging.config
from Logs.log_config import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger('main')