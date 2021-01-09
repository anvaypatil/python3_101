from random import randint


def merge(left, right):
    ll: int = 0
    rr: int = 0
    arr = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            arr.append(left[ll])
            ll += 1
        else:
            arr.append(right[rr])
            rr += 1

    arr += left[ll:]
    arr += right[rr:]

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    else:
        return arr


if __name__ == '__main__':
    a = [randint(1, 100) for _ in range(20)]
    print(a)
    print(merge_sort(a))
