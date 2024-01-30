import atexit
import json
import logging
import logging.config
import pathlib
import jsonLogger

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream" : "ext://sys.stdout"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "hanlders": ["stdout"]
        }
    }
}
logger = logging.getLogger("my_app")

def setup_logging():
    config_file = pathlib.Path("logging.config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    # logging.config.dictConfig(config)
    # queue_handler = logging.getHandlerByName("queue_handler")
    # if queue_handler is not None:
    #     queue_handler.listener.start()
    #     atexit.register(queue_handler.listener.stop)


if __name__ == '__main__':
    setup_logging()
    logger.error("Ciaone", extra={"something_else": 14})