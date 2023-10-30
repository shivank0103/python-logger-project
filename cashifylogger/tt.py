from cashifylogger import CashifyLogger
from fluent_logger import ab


def t1():
    ab()
    a = CashifyLogger(etcd_host='', etcd_port=80, etcd_protocol='https', service_name='', service_version='v1')
    a.info('working')
    try:
        25/0
        # a.error('error test')
    except Exception as e:
        a.error('some error occured')
        a.info('a')


if __name__ == '__main__':
    print(t1())
