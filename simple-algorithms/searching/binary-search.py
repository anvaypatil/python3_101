import random
from bisect import bisect, bisect_left, bisect_right


def index(arr, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    raise ValueError


def find_lt(arr, x):
    'Find rightmost value less than x'
    i = bisect_left(arr, x)
    if i:
        return arr[i - 1]
    raise ValueError


def find_le(arr, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(arr, x)
    if i:
        return arr[i - 1]
    raise ValueError


def find_gt(arr, x):
    'Find leftmost value greater than x'
    i = bisect_right(arr, x)
    if i != len(arr):
        return arr[i]
    raise ValueError


def find_ge(arr, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(arr, x)
    if i != len(arr):
        return arr[i]
    raise ValueError


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    'get grades of students'
    i = bisect(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    arr = [22, 46, 51, 52, 58, 67, 83, 87, 92, 94]  # sorted(random.sample(range(1, 100), 10))
    print(index(arr, 51))
    print(find_lt(arr, 50))
    print(find_le(arr, 52))
    print(find_gt(arr, 56))
    print(find_ge(arr, 58))
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
