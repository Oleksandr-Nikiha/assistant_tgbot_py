from datetime import datetime, timedelta


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


def memorize_stamp(func):
    cache = {}
    stamp = {}

    def wrapper(*args):
        if args in cache:
            if datetime.now() - stamp[args] > timedelta(hours=1):
                result = func(*args)
                cache[args] = result
                stamp[args] = datetime.now()
                return result
            else:
                return cache[args]
        else:
            stamp[args] = datetime.now()
            result = func(*args)
            cache[args] = result
            return result

    return wrapper
