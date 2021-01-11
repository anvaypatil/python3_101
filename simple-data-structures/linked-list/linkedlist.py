from collections import deque

"""
Python deque from collection's module uses linked-list internally. 
https://github.com/python/cpython/blob/master/Modules/_collectionsmodule.c#L71
"""


def linked_list_operations():
    linked_list = deque(['B', 'O', '2', '3', 'H', 'I'])
    # insert into linked_list
    linked_list.append('4')
    linked_list.appendleft('7')
    linked_list.append('A')
    linked_list.append('K')
    # index of item in linked_list
    if '4' in linked_list:
        print(linked_list.index('4'))

    print(linked_list)
    # delete of item in linked_list
    linked_list.remove('2')
    print(linked_list)
    # pop elements from linked_list left and right
    linked_list.pop()
    print(linked_list)
    linked_list.popleft()
    print(linked_list)
    # insert element at position '2'
    linked_list.insert(2, 'E')
    linked_list.insert(2, 'O')
    linked_list.insert(2, 'Y')

    print(linked_list)
    print(linked_list.count('E'))

    linked_list.rotate(2)
    print(linked_list)
    # reverse a linked list
    linked_list.reverse()
    print(linked_list)


if __name__ == '__main__':
    linked_list_operations()
