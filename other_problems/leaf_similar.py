class treeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value: int = value
        self.left: treeNode | None = left
        self.right: treeNode | None = right


def are_leaf_similar(tree_a: treeNode, tree_b: treeNode) -> bool:

    def get_leaf_sequence(tree: treeNode, leaf_sequence: list[int]) -> None:
        if not tree.left and not tree.right:
            leaf_sequence.append(tree.value)
            return
        if tree.left:
            get_leaf_sequence(tree.left, leaf_sequence)
        if tree.right:
            get_leaf_sequence(tree.right, leaf_sequence)

    leaf_sequence_a = []
    get_leaf_sequence(tree_a, leaf_sequence_a)
    index = -1

    def compare(tree: treeNode, leaf_sequence: list[int], index: int) -> bool:
        if index == len(leaf_sequence):
            return False
        if not tree.left and not tree.right:
            if tree.value != leaf_sequence[index]:
                return False
            index += 1
            return True
        if tree.left and tree.right:
            return compare(tree.left, leaf_sequence, index) and compare(
                tree.right, leaf_sequence, index
            )
        if tree.left:
            return compare(tree.left, leaf_sequence, index)
        if tree.right:
            return compare(tree.right, leaf_sequence, index)
        return True

    return compare(tree_b, leaf_sequence_a, index)
