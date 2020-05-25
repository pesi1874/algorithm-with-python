from SortingAlgorithm.utils import count_time, gen_random_list, base_log


@count_time
@base_log
def selection_sort(nums):
    length = len(nums)
    for i in range(length-1):
        # print(i)
        _min = i
        for j in range(i+1, length):
            # print(j, least)
            if nums[j] < nums[_min]:
                _min = j
        nums[_min], nums[i] = nums[i], nums[_min]
        # print(nums)
    return nums


if __name__ == '__main__':
    nums = [3, 2, 6, 5, 1]
    nums = gen_random_list(1000)
    selection_sort(nums)
    '''
    原理：
    首先设置一个最小元素的索引，将列表剩余部分与它进行对比，如果存在更小的元素，则将
    该元素“挑选”出来，最后交换一开始设置的最小元素和挑选出来的元素的位置，
    这样每次遍历结束都会将最小元素移至最左侧，该元素与先前的元素构成已排序列表，剩余
    的为未排序列表
    
    详解：
    第一层循环第一次遍历时，设置最小元素least的索引为0.第二层循环会产生索引值1,2,3,4，
    分别与最小元素进行比较，即将3分别与2,6,5,1进行比较。若存在比设置的最小元素更小的元素
    ，则更新least为该元素。当第二层循环遍历结束时，交换该最小元素least与i的位置，此时
    得到的列表为[1,2,6,5,3],即在这个过程中，只交换了索引值为0和索引值为4的元素的位置，
    此时[1]为已排序的列表，[2,6,5,3]为未排序的列表。第一层循环第二次遍历时，设置最小元素
    least的索引为1，将其继续与剩余索引值为[2,3,4]的部分进行比较.第一层循环第二次遍历
    结束后，得到已排序列表[1,2],未排序列表[3,5,6],以此类推，最终排完整个列表。
    
    特殊处理：
    1.列表长度为0:
        range()函数传入数字小于等于0时不进入循环
    2.列表本身已排好序
        无，仍然会遍历所有元素
    时间复杂度：
    
    '''

