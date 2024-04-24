from loguru import logger
from functools import wraps
class Signal:
    def __init__(self, trace=False):
        self._observers = []
        self.trace = trace
    
    def subject(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug(f'Call with {args} and {kwargs}')
            func(*args, **kwargs)
            self.notify()
        return wrapper

    def subscriber(self, func):
        self._observers.append(func) 
        return func
    
    def notify(self):
        for observer in self._observers:
            observer()
