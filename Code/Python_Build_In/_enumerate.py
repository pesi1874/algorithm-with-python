#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _enumerate(iterable_data):
    return zip((i for i in range(len(list(iterable_data)))), iterable_data)


if __name__ == '__main__':
    import random

    l = [random.randint(1, 10) for i in range(20)]
    # for i, j in _enumerate(l):
    #     print(i, j)

    print(zip(1, 2))
