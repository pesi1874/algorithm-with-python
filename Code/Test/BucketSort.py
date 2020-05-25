import math


# @count_time
# @base_log
def bucket_sort(nums, bucket_size=5):
    length = len(nums)
    if length == 0:
        return nums

    min_value = nums[0]
    max_value = nums[0]
    for i in range(length):
        if i < min_value:
            min_value = nums[i]
        elif i > max_value:
            max_value = nums[i]
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    print(bucket_count, max_value, min_value)
    buckets = [[] for i in range(bucket_count)]

    # for i in range(length):
    #     print(i)
    #     buckets[math.floor((nums[i] - min_value) / bucket_size)].append(nums[i])

    # sorted_nums = []
    # for i in range(bucket_count):
    #     insertion_sort(buckets[i])
    #     for j in range(len(buckets[i])):
    #         sorted_nums.append(buckets[i][j])
    # return sorted_nums


if __name__ == '__main__':
    nums = [0, 6, 3, 11, 8, 19, 10, 3, 11, 10, 20, 1, 9, 2, 11, 1, 16, 14, 11, 5]
    bucket_sort(nums)