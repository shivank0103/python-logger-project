from abc import ABC

from cashifyetcd import CashifyETCD


class SingleTonETCD(object):
    _instance = None
    _etcd = None

    def __new__(cls, etcd_host: str, etcd_port: int, etcd_protocol: str, service_name: str, service_version: str):
        if cls._instance is None:
            cls._instance = super(SingleTonETCD, cls).__new__(cls)
            cls._etcd = CashifyETCD(
                host=etcd_host, protocol=etcd_protocol, port=etcd_port,
                service_version=service_version, service_name=service_name
            )
        return cls._etcd


class BaseLogger(ABC):

    etcd = None
    service_name = None
    service_version = None

    def __init__(self, etcd_host: str, etcd_port: int, etcd_protocol: str, service_name: str, service_version: str):
        self.etcd = SingleTonETCD(
            etcd_host=etcd_host, etcd_port=etcd_port, etcd_protocol=etcd_protocol,
            service_name=service_name, service_version=service_version
        )
        self.service_name = service_name
        self.service_version = service_version

    def set_level(self):
        pass

    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def critical(self, msg):
        pass
