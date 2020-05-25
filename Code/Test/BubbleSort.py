from SortingAlgorithm.utils import count_time, base_log


@count_time
@base_log
def bubble_sort(nums):
    length = len(nums)
    for i in range(length-1):
        print(i)
        swapped = False
        for j in range(length-1-i):
            print(j, j+1)
            if nums[j] > nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
            print('>', nums)
        if not swapped:
            break
    return nums


if __name__ == '__main__':
    nums = [3, 2, 6, 5, 1]
    # nums = gen_random_list(1000)
    result = bubble_sort(nums)
    '''
    原理：
    冒泡排序（bubble sort），也称下沉排序(sinking sort)
    通过对未排序的列表进行遍历，每次遍历时比较相邻的两个元素大小，将较大的元素交换
    至右侧，这样每次遍历结束都会将最大的元素移至列表的最右侧，该元素及先前的元素
    成为已排序列表，剩余的为未排序列表。
    
    详解：
    第一层循环第一次遍历时，未排序的列表为:[3, 2, 6, 5, 1],第二层循环会产生出
    关于该未排序列表的每两个元素的索引，即会产生0和1,1和2,2和3,3和4,然后比较每两个元素
    的大小，将较大的元素交换至右侧.这样第一层循环第一次遍历之后就会得到列表[2,3,5,1,6],
    此时[2,3,5,1]为未排序的列表，[6]为已排序的列表，故进行第二次遍历时，只会遍历
    未排序的列表，所以第一层循环第二次遍历时，第二层循环会产生0和1,1和2,2和3，
    最后第一层循环第二次遍历之后就会得到列表[2,3,1,5,6],此时[2,3,1]为为排序的列表
    [5,6]为已排序的列表.以此类推最终排完整个列表。
    
    特殊处理：
    1.列表长度为0
        range()函数传入数字小于等于0时不进入循环
    2.列表本身已排好序
        使用swapped参数进行控制，若每次遍历至少进行了一次数字交换，则标记为True
        否则，说明该列表已排好序，终止循环。
    '''