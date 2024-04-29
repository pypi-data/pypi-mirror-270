from basic_data_structure import Stack


def init_from_iterable() -> None:
    print('Init from iterable:')

    stack = Stack(0, 1, 2, 3, 4, 5)
    # or like this:
    # stack = Stack(*[0, 1, 2, 3, 4, 5])
    # stack = Stack(*range(6))

    while stack:
        value = stack.pop()
        print(value, end=' ')

    print('')


def manual_pushing() -> None:
    print('Manual pushing:')

    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')

    while stack:
        value = stack.pop()
        print(value, end=' ')

    print('')


def main() -> None:
    init_from_iterable()
    manual_pushing()


if __name__ == '__main__':
    main()
