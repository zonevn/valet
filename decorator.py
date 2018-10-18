import functools


def singleton(claz):
    inst = {}
    functools.wraps(claz)

    def new_function(*arg, **kwargs):
        if claz not in inst:
            inst[claz] = claz(*arg, **kwargs)
        return inst[claz]

    return new_function


def sync(lock):
    def generator(func):
        functools.wraps(func)

        def new_function(*args, **kargs):
            lock.acquire()
            try:
                return func(*args, **kargs)
            finally:
                lock.release()

        return new_function

    return generator
