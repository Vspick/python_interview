from functools import wraps


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def singleton(cls):
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances.keys():
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


class MySingleton(Singleton):
    a = 1

    def say(self, words):
        print(words)


@singleton
class MySingleton2(object):
    a = 1

    def say(self, words):
        print(words)


if __name__ == "__main__":
    a = MySingleton()
    b = MySingleton()
    a.say("hello")
    b.say("world")
    print("%s, %s" % (id(a), id(b)))
