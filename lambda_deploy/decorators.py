from functools import wraps


def lambda_function(f):

    @wraps(f)
    def decorted_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function
