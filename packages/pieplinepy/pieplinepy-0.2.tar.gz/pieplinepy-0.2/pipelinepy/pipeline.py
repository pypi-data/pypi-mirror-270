"""Pipeline module for chaining and executing a sequence of data transformations declaratively. """

from .transformations import Transformation, Lambda


class Pipeline:
    """
    A class for chaining and executing a sequence of data transformations declaratively.

    This class facilitates the creation and management of a pipeline designed to apply
      a series of transformations to data. Each transformation may utilize a shared context
      to perform data manipulations based on dynamic conditions. The pipeline supports hooks for
      additional operations executed before and after each transformation, allowing for extensive
      customization of data processing workflows.

    Attributes:
        context (dict, optional): A dictionary holding contextual information accessible by each transformation.
        operations (list): A list storing each operation and its metadata.
        pre_hooks (list): A list of functions to be called before each transformation.
        post_hooks (list): A list of functions to be called after each transformation.

    Parameters:
        context (dict, optional): A dictionary with data that might be required by
          transformations during pipeline execution.
    """

    def __init__(self, context=None):
        """
        Initializes the Pipeline with an optional context.

        Args:
            context (dict, optional): A dictionary to hold context that transformations might use.
        """
        self.data = None
        self.context = context if context is not None else {}
        self.operations = []
        self.pre_hooks = []
        self.post_hooks = []

    def stage(self, transformation, *args, description=None, **kwargs):
        """
        Adds a transformation stage to the pipeline.

        This method wraps a callable transformation with metadata and appends it to
        the pipeline's operations list. If the callable is not an instance of Transformation,
        it is wrapped using the Lambda class.

        Args:
            transformation (callable or Transformation): The transformation function or an instance of Transformation.
            *args: Arguments to pass to the transformation constructor.
            description (str, optional): A brief description of the transformation for documentation purposes.
            **kwargs: Keyword arguments to pass to the transformation constructor.

        Returns:
            Pipeline: Returns the instance of the Pipeline to allow method chaining.

        Raises:
            TypeError: If the transformation cannot be initialized with the provided arguments.
        """
        if callable(transformation) and not isinstance(transformation, Transformation):
            try:
                transformation = transformation(*args, **kwargs)
            except TypeError:
                transformation = Lambda(transformation)
        elif not isinstance(transformation, Transformation):
            transformation = Lambda(transformation)

        self.operations.append({"transformation": transformation, "description": description})
        return self

    def add_pre_hook(self, hook):
        """
        Adds a function to be called before each transformation is applied.

        Args:
            hook (callable): The function to be called.

        Returns:
            Pipeline: Returns the instance of the Pipeline to allow method chaining.
        """
        self.pre_hooks.append(hook)
        return self

    def add_post_hook(self, hook):
        """
        Adds a function to be called after each transformation is applied.

        Args:
            hook (callable): The function to be called.

        Returns:
            Pipeline: Returns the instance of the Pipeline to allow method chaining.
        """
        self.post_hooks.append(hook)
        return self

    def run(self):
        """
        Executes all the stages in the pipeline in the order they were added.

        Processes the data through each stage, utilizing pre and post hooks for
        additional operations. This method iterates through each stored operation
        and applies the transformation to the data.

        Returns:
            The transformed data as processed by the entire pipeline.

        Raises:
            ValueError: If no initial data has been set in the pipeline before execution.
        """
        result = self.data
        for operation_info in self.operations:
            operation = operation_info["transformation"]
            for hook in self.pre_hooks:
                hook(result, self.context, operation_info)
            result = operation.apply(result, self.context)
            for hook in self.post_hooks:
                hook(result, self.context, operation_info)
        return result

    def __repr__(self):
        """
        Provides a string representation of the pipeline's execution result.

        Returns:
            str: The string representation of the result after the pipeline has been executed.
        """
        return f"{self.run()}"
