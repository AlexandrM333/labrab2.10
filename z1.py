#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sred_geom(*args):
    if not args:
        return None

    multi = 1
    for i in args:
        multi *= i
    sr_gm = pow(multi, 1/len(args))
    return float(sr_gm)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа : ").split()))
    print(sred_geom(*list_n))
