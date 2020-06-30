from Code.utils import count_time, base_log


# @count_time
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
    '''
    原理：
    冒泡排序（bubble sort），也称下沉排序(sinking sort)
    通过对未排序的列表进行遍历，每次遍历时比较相邻的两个元素大小，将较大的元素交换
    至右侧，这样每次遍历结束都会将最大的元素移至列表的最右侧，该元素及先前的元素
    成为已排序列表，剩余的为未排序列表。
    
    详解：
    
    
    特殊处理：
    1.列表长度为0
        range()函数传入数字小于等于0时不进入循环
    2.列表本身已排好序
        使用swapped参数进行控制，若每次遍历至少进行了一次数字交换，则标记为True
        否则，说明该列表已排好序，终止循环。
    '''