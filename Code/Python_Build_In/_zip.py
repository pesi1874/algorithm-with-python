#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable


class _zip:
    def __init__(self, *args):
        for i in args:
            if not isinstance(i, Iterable):
                raise TypeError(" zip argument #{} must support iteration".format(i))

    def __next__(self):
        return


if __name__ == '__main__':
    for i, j in _zip("ww", "2"):
        print(i, j)

    pass
