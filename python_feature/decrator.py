from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start func, %s" % func.__name__)
        res = func(*args, **kwargs)
        print("end func, %s" % func.__name__)
        return res
    return wrapper


def log2(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("[%s]start func %s" % (text, func.__name__))
            res = func(*args, **kwargs)
            print("[%s]start func %s" % (text, func.__name__))
            return res
        return wrapper
    return decorator


@log2("happy")
def test():
    print("TEST")
    a = 1
    return a


if __name__ == "__main__":
    x = test()
    print(x)