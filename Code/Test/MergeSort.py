from SortingAlgorithm.utils import count_time, base_log


def merge_sort(nums):
    print(nums)
    length = len(nums)
    if length <= 1:
        return nums
    num = int(length/2)
    left = merge_sort(nums[:num])
    right = merge_sort(nums[num:])
    print('merge', left, right)
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    sorted_nums = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_nums.append(left[l])
            l += 1
        else:
            sorted_nums.append(right[r])
            r += 1
    sorted_nums += left[l:]
    sorted_nums += right[r:]
    return sorted_nums


if __name__ == '__main__':
    nums = [3, 2, 6, 5, 1]
    # nums = [0, 6, 3, 11, 8, 19, 10, 3, 11, 10, 20, 1, 9, 2, 11, 1, 16, 14, 11, 5]
    # nums = gen_random_list(1000000)
    c = count_time(base_log(merge_sort))
    c(nums)
    '''
    原理：
    归并排序（合并排序），采用分治的策略，先确定列表的中位数，然后将待排序的列表一分为二（左右），
    然后递归继续分解待排序列表，直到列表长度小于等于1时，开始进行合并。合并时，同时遍历左右两个列表，
    比较两个列表第一位元素的大小，较小的元素则放入新的列表中，然后在取出较小元素的列表中继续往后取元素。
    直到其中一个列表为空，则将另一个列表剩余的所有元素依次放入新列表末尾
    
    详解：
    首先求出待排序列表的中位数num，例子中的num=2，第一次递归得到左半部分为[3,2],右半部分为
    [6,5,1]，对两部分列表继续进行递归分解，左半部分最终得到的结果可以用
    left = merge_sort(nums[:num])表示，同理可得右半部分的表示。在执行left的函数时，
    [3,2]会进行第二次递归拆解成左半部分[3]，右半部分[2]，此时列表大小已经为1，故无法
    再进行merge_sort函数的拆解，所以开始合并，执行return merge(left, right)
    在merge函数中，合并第二次递归生成的左半部分[3]和右半部分[2]最终会得到返回值[2,3]，
    同理可得第一次递归右半部分最后的返回结果为[1,5,6]，最后合并第一次递归产生的两部分。
    
    特殊处理:
    
    算法复杂度：
    时间：
    '''