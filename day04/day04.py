from itertools import groupby
from functools import reduce


def check_num(num: str):
    grows = all(l <= r for l, r in zip(num[0:-1], num[1:]))
    double = any(l == r for l, r in zip(num[0:-1], num[1:]))
    return grows and double


def find_all(lower, upper, check):
    return sum(1 for i in range(lower, upper + 1) if check(str(i)))


def check_num2(num: str):
    grows = all(l <= r for l, r in zip(num[0:-1], num[1:]))
    double = any(sum(1 for _ in vs) == 2 for _, vs in groupby(num))
    return grows and double
