from doorman import permissions


def register(name_or_test_func=None):
    if callable(name_or_test_func):
        permissions.register(name_or_test_func.__name__, name_or_test_func)
        return name_or_test_func
    else:
        def decorator(test_func):
            permissions.register(name_or_test_func, test_func)
            return test_func
        return decorator
