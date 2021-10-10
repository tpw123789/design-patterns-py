import logging

logging.basicConfig(level=logging.INFO)


def logging_decorator(func):
    """紀錄日誌的裝飾器"""
    def wrapper_logging(*args, **kwargs):
        logging.info(f'Start {func.__name__}...')
        func(*args, *kwargs)
        logging.info(f'End {func.__name__}...')
    return wrapper_logging


@logging_decorator
def show_info(*args, **kwargs):
    print(f'This is a test func, arg: {args} kwargs: {kwargs}')


# de = logging_decorator(show_info)
# de('args1', 'args2', kwargs1=1, kwargs2=2)
show_info('args1', 'args2', kwargs1=1, kwargs2=2)

