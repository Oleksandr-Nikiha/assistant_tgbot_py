from datetime import datetime, timedelta


class MemorizeError(Exception):
    pass


def memorize(func):
    cache = {}

    def wrapper(*args):
        try:
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        except Exception as e:
            raise MemorizeError(f"Error in memorized function: {e}")

    return wrapper


def memorize_stamp(func):
    cache = {}
    stamp = {}

    def wrapper(*args):
        try:
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
        except Exception as e:
            raise MemorizeError(f"Error in stamped memorized function: {e}")

    return wrapper
