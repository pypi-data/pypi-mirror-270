from typing import Any, Self


class ListNode:
    """A node of a linked list."""

    def __init__(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
        next: Self | None = None,  # noqa: WPS125 Found builtin shadowing: next
    ):
        """Init a list node.

        Parameters:
            value: a value of the node
            next: (optional) next node
        """
        self.value = value  # noqa: WPS110 Found wrong variable name
        self.next = next
