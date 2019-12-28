import logging
import logging.config
import yaml
import os


class Log:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def setup_logging():
        log_yaml_path = os.path.dirname(os.path.abspath(__file__))
        default_file = os.path.join(log_yaml_path, 'logging_config.yaml')

        default_level = logging.INFO

        if os.path.exists(default_file):
            with open(default_file, 'r') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)