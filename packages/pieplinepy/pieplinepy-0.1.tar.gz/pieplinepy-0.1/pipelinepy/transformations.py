from abc import ABC, abstractmethod
import inspect
from functools import wraps

class Transformation(ABC):
    @abstractmethod
    def apply(self, data, context):
        """Apply the transformation to the data and optionally use the context."""
        pass

def context_aware(function):
    @wraps(function)
    def wrapper(data, context=None, *args, **kwargs):
        params = inspect.signature(function).parameters
        if 'context' in params:
            return function(data, context, *args, **kwargs)
        else:
            return function(data, *args, **kwargs)
    return wrapper

class Lambda(Transformation):
    def __init__(self, function, *args, **kwargs):
        # Wrap the function to be context-aware
        self.function = context_aware(function)
        self.args = args
        self.kwargs = kwargs

    def apply(self, data, context=None):
        return self.function(data, context, *self.args, **self.kwargs)
    
