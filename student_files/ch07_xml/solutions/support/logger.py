import logging

my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)
handler1 = logging.FileHandler('./lab05_logfile.log')
formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M:%S')
handler1.setFormatter(formatter)
my_logger.addHandler(handler1)

# handler 2 is used to log to the console if desired
# handler2 = logging.StreamHandler()
# handler2.setFormatter(formatter)
# my_logger.addHandler(handler2)


def log(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        my_logger.info('{0} called passing args: {1}'.format(func.__name__, ' '.join([str(arg) for arg in args[1:]])))
        return ret
    return wrapper