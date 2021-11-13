from time import time

def my_perf(func):
    def wrapper(*args,**kwargs):
        t1= time()
        res = func(*args,**kwargs)
        t2=time()
        print(f'took {t2-t1} s')
        return res
    return wrapper

@my_perf
def iteration():
    for i in range(1000000):
        i*5

iteration()