#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    t = tuple(map(int, input().split()))

    index_last = -1
    troyki = list(zip(t, t[1:], t[2:]))
    predsh = []
    promezh = []

    for i in troyki:
        if i[1] > i[0] and i[1] > i[2]:
            predsh += promezh
            promezh = []
        else:
            promezh += [i[0]]

    print(tuple(predsh))
