import collections
import itertools

# Straight from https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def count_increments(measurements, window_size):
    windows = sliding_window(measurements, window_size)
    pairs = itertools.pairwise(windows)
    return sum([1 for p in pairs if sum(p[1]) > sum(p[0])])