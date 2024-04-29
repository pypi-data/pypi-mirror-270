from typing import Generator

from basic_data_structure import TreeNode


def generate_tree() -> TreeNode:
    """Generate binary tree.

                 8
          ┌──────┴───────┐
          4              12
      ┌───┴───┐       ┌───┴───┐
      2       6       10      14
    ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    1   3   5   7   9   11  13  15
    """
    return TreeNode(
        8,
        left=TreeNode(
            4,
            left=TreeNode(
                2,
                left=TreeNode(1),
                right=TreeNode(3),
            ),
            right=TreeNode(
                6,
                left=TreeNode(5),
                right=TreeNode(7),
            ),
        ),
        right=TreeNode(
            12,
            left=TreeNode(
                10,
                left=TreeNode(9),
                right=TreeNode(11),
            ),
            right=TreeNode(
                14,
                left=TreeNode(13),
                right=TreeNode(15),
            ),
        ),
    )


def dfs(root: TreeNode | None) -> Generator[int, None, None]:
    """Depth-first search."""
    if root:
        if root.left:
            yield from dfs(root.left)

        yield root.value

        if root.right:
            yield from dfs(root.right)


def main():
    print('Depth-first search (DFS)')
    for data in dfs(root=generate_tree()):
        print(data, end=' ')


if __name__ == '__main__':
    main()
