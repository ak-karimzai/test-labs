log_config = {
    'version': 1,
    'formatters': {
        'main_formatter': {
            'format': '[%(asctime)s]: %(levelname)s %(pathname)s func: %(funcName)s "%(message)s"',
        },
    },
    'handlers': {
        'main_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': 'main.log',
            'encoding': 'UTF-8',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['main_handler'],
            'level': 'DEBUG',
        },
    },
}
