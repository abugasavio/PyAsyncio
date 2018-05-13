import threading
import time
import logging


def deamon():
    logging.debug('starting')
    time.sleep(0.2)
    logging.debug('exiting')


def non_deamon():
    logging.debug('starting')
    logging.debug('exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


d = threading.Thread(target=deamon, name='daemon', daemon=True)


t = threading.Thread(target=non_deamon, name='non-daemon')


d.start()
t.start()
