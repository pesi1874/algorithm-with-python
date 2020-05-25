from SortingAlgorithm.utils import count_time, base_log


# @count_time
# @base_log
def quick_sort_standord(array,low,high):
    if low < high:
        key_index = partion(array,low,high)
        # print(key_index)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)


def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


if __name__ == '__main__':
    nums = [3, 2, 6, 5, 1]
    # array2 = gen_random_list(10000)
    print(quick_sort_standord(nums,0,len(nums)-1))
