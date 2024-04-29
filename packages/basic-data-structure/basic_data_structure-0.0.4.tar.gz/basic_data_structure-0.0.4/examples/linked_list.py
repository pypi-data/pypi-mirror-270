from basic_data_structure import ListNode


def generate_list(size: int) -> ListNode | None:
    """Generate linked list of N nodes.

    0 → 1 → 2 → 3 → ... → N
    """
    assert size >= 0
    dummy = ListNode(None)
    pointer = dummy
    for i in range(size):
        pointer.next = ListNode(i)
        pointer = pointer.next
    return dummy.next


def print_list(head: ListNode | None) -> None:
    while head:
        print(head.value, end=' → ' if head.next else '\n')
        head = head.next


def main() -> None:
    print_list(head=generate_list(5))


if __name__ == '__main__':
    main()
