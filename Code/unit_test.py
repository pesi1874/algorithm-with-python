#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Code.utils import gen_random_list


def quick_sort():
    from Algorithm.Sort.QuickSort import quick_sort
    cols = [3, 2, 6, 5, 1]
    cols = gen_random_list(10000)
    quick_sort(cols)

def bubble_sort():
    from Algorithm.Sort.BubbleSort import bubble_sort
    cols = [3, 2, 6, 5, 1]
    bubble_sort(cols)


if __name__ == '__main__':
    quick_sort()
