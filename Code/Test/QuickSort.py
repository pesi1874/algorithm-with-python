from SortingAlgorithm.utils import count_time, base_log, gen_random_list


# @count_time
# @base_log
def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    pivot = nums[0]
    bigger = []
    smaller = []
    for i in nums[1:]:
        if i > pivot:
            bigger.append(i)
        else:
            smaller.append(i)
    # print('bigger > ', bigger)
    # print('pivot > ', pivot)
    # print('smaller > ', smaller)
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


if __name__ == '__main__':
    # nums = [3, 2, 6, 5, 1]
    nums = gen_random_list(1000000)
    c = count_time(base_log(quick_sort))
    c(nums)
    '''
    原理：
    采用分治的策略，首先确定一个基准元素，然后遍历除了该基准元素外的所有元素，分别与基准元素作比较。
    若比基准元素大则放在一个新的列表中，否则放在另一个列表中。使用递归的概念对分出来的两个新列表继续
    排序。
    
    详解：
    首先将基准元素直接设置为待排序列表的第一个元素（但是可能会出现最糟情况），此时pivot=3，创建一个
    存放比该基准元素大的列表和一个存放比该基准元素小的列表，遍历剩下的所有元素，与基准元素3作比较。得到
    bigger列表[6,5],smaller列表[2,1]。此时return的返回值为quick_sort(smaller) + [pivot]
     + quick_sort(bigger),递归继续执行quick_sort(smaller) 和 quick_sort(bigger)，
     quick_sort(bigger)的返回值为[5]+[6],quick_sort(smaller)的返回值为[1]+[2],最后得到
     quick_sort(smaller)（[1]+[2]）+[3]+quick_sort(bigger)([5,6])
    
    特殊处理：
    1.列表长度为0
        if length <= 1 直接返回列表
    2.列表本身已排好序
    '''