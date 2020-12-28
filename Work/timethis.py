def timethis(func):
    import time
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print('{}.{}: {}'.format(func.__module__,func.__name__,end-start))
    return wrapper
