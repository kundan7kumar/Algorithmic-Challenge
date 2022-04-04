# Given a non-negative integer x, compute and return the square root of x
import math
from math import floor, ceil


def sqrt(x):
    x = x ** 0.5
    return int(floor(x))


print(sqrt(5))


# using math function

def sqrt1(y):
    y = math.sqrt(y)
    return int(y)


print(sqrt1(11))

# Using Pocket calculator Algorithm
# Sqrt(x) = e^(0.5)log(x)

from math import e, log


def sqrt2(z):
    if z < 2:
        return z

    left = int(e ** (0.5 * log(z)))
    right = left + 1

    return left if right * right > z else right


print(sqrt2(16))


# Time : O(1)
# Space: O(1)

# Using Binary Search Algorithm
def sqrt3(w):
    if w < 2:
        return w
    left, right = 2, w // 2

    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num > w:
            right = pivot - 1
        elif num < w:
            left = pivot + 1
        else:
            return pivot

    return right


print(sqrt3(16))


# Using Newton Rapshon Algorithm
def sqrt4(a):
    if a < 2:
        return a
    a0 = a
    a1 = (a0 + a / a0) / 2
    while abs(a0 - a1) >= 1:
        a0 = a1
        a1 = (a0 + a / a0) / 2

    return int(a1)


print(sqrt4(25))


# Time : O(log N)
# Space: O(1)

# Using Recursion and Bit
def sqrt5(b):
    if b < 2:
        return b
    left = sqrt5(b >> 2) << 1
    right = left + 1
    return left if right * right > b else right


print(sqrt5(36))
