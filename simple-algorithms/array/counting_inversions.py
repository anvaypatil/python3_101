from random import sample


def count_merge(left, right):
    ll: int = 0
    rr: int = 0
    arr = []
    inv = []
    while ll < len(left) and rr < len(right):
        if left[ll] <= right[rr]:
            arr.append(left[ll])
            ll += 1
        else:
            arr.append(right[rr])
            for i in range(ll, len(left)):
                inv.append((left[i], right[rr]))
            rr += 1

    arr += left[ll:]
    arr += right[rr:]
    return inv, arr


def counting_inversions(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        inv_left, left = counting_inversions(arr[:mid])
        inv_right, right = counting_inversions(arr[mid:])
        inv, result = count_merge(left, right)
        return inv + inv_left + inv_right, result
    else:
        return [], arr


if __name__ == '__main__':
    a = sample(range(1, 100), 4)
    b = list(reversed(sorted(a)))
    print(b)
    (inv, _) = counting_inversions(b)
    print(len(inv))
    print(inv)
