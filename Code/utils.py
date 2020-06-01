import random
import time


def count_time(func):
    """
    :rtype: object
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print('spend >>> %s seconds' % total_time)
        return result
    return wrapper


def base_log(func):
    """
    :rtype: object
    """
    def wrapper(*args, **kwargs):
        print('origin >>> ', args[0])
        result = func(*args, **kwargs)
        print('result >>> ', result)
        return result
    return wrapper


def gen_random_list(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(0, num))
    return nums

