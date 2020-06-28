import random
import time
from datetime import datetime

def count_time(func):
    """
    :rtype: object
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now().timestamp()
        result = func(*args, **kwargs)
        total_time = datetime.now().timestamp() - start_time
        print('>>> spend: %s seconds' % total_time)
        return result
    return wrapper


def base_log(func):
    """
    :rtype: object
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('--- raw: ', args[0], 'res: ', result, ' ---')
        return result
    return wrapper


def gen_random_list(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(0, num))
    return nums

