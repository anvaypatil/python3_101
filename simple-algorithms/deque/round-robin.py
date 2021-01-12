from collections import deque


def round_robin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()


if __name__ == '__main__':
    seq = list(round_robin('ABC', 'D', 'EFG', 'HIJK'))
    print(seq)
