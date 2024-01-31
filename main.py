import atexit
import json
import logging
import logging.config
import pathlib

# example of usage grafana/loki api when you need push any log/message from your python scipt
import requests
import json
import datetime


def setup_logging():
    config_file = pathlib.Path("logging.config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger()
    # logger.error("Ciao")
    logger.error("Ciaone666", extra={"something_else": 14})