def stack_using_deque():
    stack = list()
    stack.append('A')
    stack.append('P')
    stack.append('Q')
    stack.append('R')
    print(stack)
    # pop element from top of stack
    stack.pop()
    print(stack)
    # peek element from top of stack
    print(stack[len(stack) - 1])


def stack_using_list():
    pass


if __name__ == '__main__':
    stack_using_list()
    stack_using_deque()
