SIZE = 5
from math import factorial
import zlib, base64 as b

import pprint

from decs import debug
from typing import List

factorial = debug(factorial)


def zig(size: int)-> List[List[int]]:
    inner = lambda x, y: max(max(max(x, y), size - x - 1), size - y - 1)
    return [[size - inner(i, j) for i in range(size)] for j in range(size)]


def is_wprime(n):
    return n > 1 and bool(n == 2 or (n % 2 and (factorial(n - 1) + 1) % n == 0))


if __name__ == "__main__":
    for row in zigga_(25):
        print(row)
