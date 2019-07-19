#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-19 10:12
# @Author  : yuguo

def fibo(x):
    if x == 0:
        resp = 0
    elif x == 1:
        resp = 1
    else:
        return fibo(x-1) + fibo(x-2)
    return resp
assert fibo(5) == 5