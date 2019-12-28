import logging
import logging.config
import functools


class LogDecorator:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def __call__(self, fn):
        @functools.wraps(fn)
        def log_decorated(*args, **kwargs):
            try:
                self.logger.info("Func: {0} - args: {1} - kwargs: {2}".format(fn.__name__, args, kwargs))
                result = fn(*args, **kwargs)
                self.logger.info(f'Func ret: {result}')
                return result
            except Exception as ex:
                self.logger.debug("Exception {0}".format(ex))
                raise ex

        return log_decorated
