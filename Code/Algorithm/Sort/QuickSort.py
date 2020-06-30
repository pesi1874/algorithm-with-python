from Code.utils import count_time, base_log

"""
边界处理：
1.集合长度<1,直接返回列表,不进入递归
"""


# @count_time
@base_log
def quick_sort(cols):
    if len(cols) <= 1:
        return cols

    pivot = cols[0]
    bigger = []
    smaller = []
    for i in cols[1:]:
        if i > pivot:
            bigger.append(i)
        else:
            smaller.append(i)
    print('> pivot: {} bigger: {} smaller: {}'.format(pivot, bigger, smaller))

    smaller = quick_sort(smaller) if len(smaller) > 1 else smaller
    bigger = quick_sort(bigger) if len(bigger) > 1 else bigger
    return smaller + [pivot] + bigger
