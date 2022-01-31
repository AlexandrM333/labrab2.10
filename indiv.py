#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def summod(*args):
    s = 0
    neg = -1
    for i, n in enumerate(args):
        if n == 0:
            neg = i
            break

    for n in args[neg + 1:]:
        s += abs(n)
    return s


if __name__ == '__main__':
    arr = list(map(int, input("Введите список: ").split()))
    print(summod(*arr))
