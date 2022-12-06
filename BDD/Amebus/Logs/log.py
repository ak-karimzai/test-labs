import logging.config
from Amebus.Logs.log_config import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger('main')