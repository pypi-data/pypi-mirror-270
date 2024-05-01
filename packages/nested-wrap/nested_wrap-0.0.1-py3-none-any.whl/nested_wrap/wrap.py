from functools import wraps

def wrap_func_with_nested_access(f, factory_f):
    """
    Before conducting actual function `f`, wrap its args and kargs into nested
    ones.

    :param f: function to be wrapped.
    :return: wrapped function
    """

    def wrap_nested_structure(*args, **kargs):
        wrapped_args = [factory_f(arg) for arg in args]
        wrapped_kargs = {
            k: factory_f(arg)
            for k, arg in kargs.items()
        }
        return wrapped_args, factory_f(wrapped_kargs)

    @wraps(f)
    def wrapped_f(*args, **kargs):
        args, kargs = wrap_nested_structure(*args, **kargs)
        # to ensure the args passing to the final calling of f can be nested,
        # in case of deeper-order wrapper funcs de-wrap this nesting behavior
        args = [
            wrap_func_with_nested_access(arg) if callable(arg) else arg
            for arg in args
        ]
        kargs = {
            k: (wrap_func_with_nested_access(arg) if callable(arg) else arg)
            for (k, arg) in kargs.items()
        }
        return f(*args, **kargs)

    return wrapped_f