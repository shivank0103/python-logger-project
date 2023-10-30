from fluent import sender

from cashifylogger.base import BaseLogger


class CashifyFluentLogger(BaseLogger):

    def log(self, msg):
        logger = sender.FluentSender('fluentd', host='172.17.0.1', port=24224)
        logger.emit(self.service_name + '_' + self.service_version, msg)
