"""
Create by 吹着风的包子 on 2019-01-28
"""
__author__ = '吹着风的包子'


def frog_jump(n=10):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return frog_jump(n - 1) + frog_jump(n - 2)


print(frog_jump(12))
