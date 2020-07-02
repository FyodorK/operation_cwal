from typing import Generator, List, Iterator


def rotation_right(seq: List[int])-> Iterator:
    return zip(*seq[::-1])


def _inner(m: int, n: int, start=1) -> Generator:
    if n == 0:
        yield ()
    else:
        yield tuple(range(start, m + start))
        for row_ in rotation_right(list(_inner(n-1, m, m + start))):
            yield row_


def spiral(m: int) -> Generator:
    return _inner(m, m)


for row in spiral(5):
    print(''.join("%3i" % i for i in row))
