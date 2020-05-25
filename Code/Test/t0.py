import random
from SortingAlgorithm.utils import count_time


@count_time
def a(nums):
    print(nums)


@count_time
def b(nums):
    for i in range(10000):
        nums[random.randint(0,999)] = nums[random.randint(0,999)]
    print(nums)


nums = [i for i in range(1000)]

# a(nums)
# b(nums)
def dec(func):
    def wrapper(*argv):
        print(argv, 'Decorated!')
        print(id(func))
        return(func(*argv))
    return(wrapper)

# @dec
def f(n):
    print(n, 'Original!')
    if n == 1: return(1)
    else: return(f(n - 1) + n)

# print(f(5))
# print(f(5))

dec_f = dec(f)
print(dec_f)
print(dec_f(5))

# print(id(f))
# f = dec(f)#f = wrapper
# print(f)
# print(f(5))

# t = dec(f)
# print(t(5))