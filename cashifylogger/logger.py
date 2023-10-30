import sys
import logging
from cashifylogger.base import BaseLogger

logger = logging.getLogger(__name__)
FORMAT_STRING = '%(asctime)s-%(levelname)s-%(message)s'
logging.basicConfig(format=FORMAT_STRING, encoding='utf-8')


class CashifyLogger(BaseLogger):

    def set_level(self):
        log_level = self.etcd.get_property_value('log.level')
        if log_level.lower() == 'info':
            logging.getLogger().setLevel(logging.INFO)
        elif log_level.lower() == 'debug':
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.getLogger().setLevel(logging.ERROR)

    def debug(self, msg):
        self.set_level()
        logger.debug(msg)

    def info(self, msg):
        self.set_level()
        logger.info(msg)
        # logger.info(msg + str(inspect.stack()[1][2]) + str(inspect.stack()[1][3]))

    def warning(self, msg):
        self.set_level()
        logger.warning(msg)

    def error(self, msg):
        self.set_level()
        logger.error(sys._getframe(1))
        logger.error(msg, exc_info=True)

    def critical(self, msg):
        self.set_level()
        logger.critical(msg)
