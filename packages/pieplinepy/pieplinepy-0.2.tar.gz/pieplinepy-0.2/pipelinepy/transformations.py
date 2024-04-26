""" 
A module containing classes and utilities for data transformations within a data processing pipeline.
"""

from abc import ABC, abstractmethod
import inspect
from functools import wraps


class Transformation(ABC):
    """
    An abstract base class defining the interface for data transformations.

    This class should be inherited by any class that aims to implement a data transformation
    within a data processing pipeline. It enforces the implementation of the `apply` method,
    ensuring that all transformations can be used interchangeably within the pipeline framework.

    Methods:
        apply(data, context): Applies a transformation to the provided data, optionally using a context.
    """

    @abstractmethod
    def apply(self, data, context):
        """
        Apply the transformation to the data.

        This method should be overridden by subclasses to implement specific data transformation logic.

        Args:
            data: The input data on which to perform the transformation.
            context (dict, optional): A dictionary containing contextual information that can influence the transformation.

        Returns:
            The transformed data.
        """


def context_aware(function):
    """
    A decorator that makes a function aware of a 'context' parameter if it exists in the function's signature.

    This decorator modifies a function so that it can conditionally accept a 'context' parameter.
    If 'context' is part of the function's parameters, it is passed along; otherwise, the function
    is called without the context.

    Args:
        function (callable): The function to be made context-aware.

    Returns:
        callable: A wrapped function that handles the context parameter intelligently.
    """

    @wraps(function)
    def wrapper(data, context=None, *args, **kwargs):
        # Inspect the function's signature to determine if 'context' is a parameter.
        params = inspect.signature(function).parameters
        if "context" in params:
            return function(data, context, *args, **kwargs)
        return function(data, *args, **kwargs)

    return wrapper


class Lambda(Transformation):
    """
    A generic transformation class that wraps a simple function to comply with the Transformation interface.

    This class is useful for integrating simple functions into a data transformation pipeline,
    particularly those functions that might not inherently support a 'context' parameter.

    Attributes:
        function (callable): The function that performs the data transformation.
        args (tuple): Additional positional arguments to pass to the function.
        kwargs (dict): Keyword arguments to pass to the function.

    Args:
        function (callable): The transformation function to be executed.
        *args: Variable positional arguments to be passed to the transformation function.
        **kwargs: Keyword arguments to be passed to the transformation function.
    """

    def __init__(self, function, *args, **kwargs):
        self.function = context_aware(function)
        self.args = args
        self.kwargs = kwargs

    def apply(self, data, context=None):
        """
        Apply the wrapped function to the data, passing along the context if applicable.

        Args:
            data: The data to transform.
            context (dict, optional): Optional context to provide additional data or parameters to the function.

        Returns:
            The result of the function application, which is considered the transformed data.
        """
        return self.function(data, context, *self.args, **self.kwargs)
