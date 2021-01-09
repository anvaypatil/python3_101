from random import randint


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort([x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + quick_sort([x for x in arr[1:] if x > arr[0]])


if __name__ == '__main__':
    a = [randint(1, 100) for _ in range(20)]
    print(a)
    print(quick_sort(a))