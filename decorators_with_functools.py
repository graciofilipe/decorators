import time
from functools import wraps
def logtime(fun):
    
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        total_time = time.time() - start_time
        with open('timelog.txt', 'a') as outfile:
            outfile.write(f'{time.time()} \t {fun.__name__} \t {total_time} \n')
        return result

    return wrapper


@logtime
def print_args(a1, a2):
    print(a1, a2)

@logtime
def sum_args(a1, a2):
    return a1 + a2


print_args('x1', 'x2')

sum_args(2, 3)


