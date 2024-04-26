from .transformations import Transformation, Lambda

class Pipeline:
    def __init__(self, data, context=None):
        self.data = data
        self.context = context if context is not None else {}
        self.operations = []
        self.pre_hooks = []
        self.post_hooks = []

    def stage(self, transformation, *args, description=None, **kwargs):
        # Wrap transformation with metadata
        if callable(transformation) and not isinstance(transformation, Transformation):
            try:
                transformation = transformation(*args, **kwargs)
            except TypeError:
                transformation = Lambda(transformation)
        elif not isinstance(transformation, Transformation):
            transformation = Lambda(transformation)

        self.operations.append({'transformation': transformation, 'description': description})
        return self

    def add_pre_hook(self, hook):
        self.pre_hooks.append(hook)
        return self

    def add_post_hook(self, hook):
        self.post_hooks.append(hook)
        return self

    def run(self):
        result = self.data
        for operation_info in self.operations:
            operation = operation_info['transformation']
            for hook in self.pre_hooks:
                hook(result, self.context, operation_info)
            result = operation.apply(result, self.context)
            for hook in self.post_hooks:
                hook(result, self.context, operation_info)
        return result

    def __repr__(self):
        return f"{self.run()}"


