"""

"""


def main():
    d1 = {'p1': 3, 'p2': 5, 'p3': 12, 'p4': 7, 'p5': 4}
    more_than_2 = ({k: v > 2 for k, v in d1.items()})
    print(all(more_than_2))


if __name__ == '__main__':
    main()
