#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sred_garm(*args):
    if not args:
        return None

    summ = 0
    a = len(args)
    for i in args:
        summ += 1/i
    x = a/summ
    return float(x)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа : ").split()))
    print(sred_garm(*list_n))
