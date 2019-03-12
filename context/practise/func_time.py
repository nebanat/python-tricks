import time
from contextlib import contextmanager


class TimeFunc:
    """
    a context manager that times the execution of a code block
    and outputs the total time the code block takes to execute


    try implementing a context manager that measures the execution time
    of a code block using the time.time function. Be sure to try out writing both a decorator-based
    and a class-based variant to drive home the difference between the two
    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('This %s took %s milliseconds to execute' % (self.name, (self.end - self.start)*1000))


@contextmanager
def time_func(func_name):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('This %s took %s milliseconds to execute' % (func_name, (end - start) * 1000))
