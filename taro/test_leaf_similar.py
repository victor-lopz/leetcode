import unittest
from leaf_similar import treeNode, are_leaf_similar


class TestLeafSimilar(unittest.TestCase):
    """
    Unit tests for the leaf_similar problem.
    Problem: Two binary trees are considered leaf-similar if their leaf value sequences are the same.
    """

    def test_identical_trees(self):
        """Test two identical trees"""
        #       3           3
        #      / \         / \
        #     5   1   vs  5   1
        tree_a = treeNode(3, treeNode(5), treeNode(1))
        tree_b = treeNode(3, treeNode(5), treeNode(1))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_different_structures_same_leaves(self):
        """Test different structures with same leaf sequence"""
        #       3           6
        #      / \         / \
        #     5   1   vs  5   1
        #                /
        #               7
        tree_a = treeNode(3, treeNode(5), treeNode(1))
        tree_b = treeNode(6, treeNode(5, treeNode(7)), treeNode(1))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_different_leaves(self):
        """Test trees with different leaf sequences"""
        #       1           1
        #      / \         / \
        #     2   3   vs  2   4
        tree_a = treeNode(1, treeNode(2), treeNode(3))
        tree_b = treeNode(1, treeNode(2), treeNode(4))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_single_node_trees(self):
        """Test single node trees (leaves are roots)"""
        tree_a = treeNode(5)
        tree_b = treeNode(5)
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_single_node_different_values(self):
        """Test single node trees with different values"""
        tree_a = treeNode(3)
        tree_b = treeNode(5)
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_left_skewed_trees_same_leaves(self):
        """Test left-skewed trees with same leaf"""
        #       1           2
        #      /           /
        #     2           3
        #    /           /
        #   3           4
        tree_a = treeNode(1, treeNode(2, treeNode(3)))
        tree_b = treeNode(2, treeNode(3, treeNode(4)))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_right_skewed_trees_same_leaves(self):
        """Test right-skewed trees with same leaf"""
        #       1             2
        #        \             \
        #         2             3
        #          \             \
        #           3             4
        tree_a = treeNode(1, None, treeNode(2, None, treeNode(3)))
        tree_b = treeNode(2, None, treeNode(3, None, treeNode(4)))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_multiple_leaves_same_sequence(self):
        """Test trees with multiple leaves in same order"""
        #         1               2
        #        / \             / \
        #       2   3           5   6
        #      / \             / \
        #     4   5           4   3
        tree_a = treeNode(1, treeNode(2, treeNode(4), treeNode(5)), treeNode(3))
        tree_b = treeNode(2, treeNode(5, treeNode(4), treeNode(3)), treeNode(6))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_multiple_leaves_different_sequence(self):
        """Test trees with multiple leaves in different order"""
        #         1               1
        #        / \             / \
        #       2   3           2   3
        #      / \             / \
        #     4   5           5   4
        tree_a = treeNode(1, treeNode(2, treeNode(4), treeNode(5)), treeNode(3))
        tree_b = treeNode(1, treeNode(2, treeNode(5), treeNode(4)), treeNode(3))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_complex_tree_a_vs_b(self):
        """Test complex trees from LeetCode example"""
        #           3                 3
        #          /                 /
        #         5                 5
        #        / \               / \
        #       6   2             6   2
        #      /   / \           /   / \
        #     7   9   8         7   9   8
        tree_a = treeNode(
            3,
            treeNode(5, treeNode(6, treeNode(7)), treeNode(2, treeNode(9), treeNode(8)))
        )
        tree_b = treeNode(
            3,
            treeNode(5, treeNode(6, treeNode(7)), treeNode(2, treeNode(9), treeNode(8)))
        )
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_leaf_sequence_4_5_7_8_vs_4_9_8(self):
        """Test different leaf sequences"""
        #         1                2
        #        / \              / \
        #       2   3            4   5
        #      / \              /
        #     4   5            6
        tree_a = treeNode(1, treeNode(2, treeNode(4), treeNode(5)), treeNode(3))
        tree_b = treeNode(2, treeNode(4, treeNode(6)), treeNode(5))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_unbalanced_vs_balanced_same_leaves(self):
        """Test unbalanced vs balanced trees with same leaves"""
        #       1             1
        #      / \           / \
        #     2   3         2   3
        #    /
        #   4
        tree_a = treeNode(1, treeNode(2, treeNode(4)), treeNode(3))
        tree_b = treeNode(1, treeNode(2), treeNode(3, treeNode(4)))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_many_leaves(self):
        """Test trees with many leaves"""
        #          1
        #        / | \
        #       2  3  4
        tree_a = treeNode(1, treeNode(2), treeNode(3))
        tree_a.right = treeNode(4)  # Add third leaf
        
        #          5
        #         / \
        #        6   7
        #       /   / \
        #      2   3   4
        tree_b = treeNode(5, treeNode(6, treeNode(2)), treeNode(7, treeNode(3), treeNode(4)))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_duplicate_leaf_values(self):
        """Test trees with duplicate leaf values"""
        #       1             2
        #      / \           / \
        #     2   2         3   2
        tree_a = treeNode(1, treeNode(2), treeNode(2))
        tree_b = treeNode(2, treeNode(3), treeNode(2))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))

    def test_duplicate_leaf_values_same(self):
        """Test trees with same duplicate leaf values"""
        #       1             2
        #      / \           / \
        #     5   5         3   5
        #                   /   /
        #                  5   5
        tree_a = treeNode(1, treeNode(5), treeNode(5))
        tree_b = treeNode(2, treeNode(3, treeNode(5)), treeNode(5))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_negative_values(self):
        """Test trees with negative values"""
        tree_a = treeNode(1, treeNode(-5), treeNode(-1))
        tree_b = treeNode(2, treeNode(-5), treeNode(-1))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_zero_values(self):
        """Test trees with zero values"""
        tree_a = treeNode(0, treeNode(0), treeNode(0))
        tree_b = treeNode(1, treeNode(0), treeNode(0))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_large_values(self):
        """Test trees with large integer values"""
        tree_a = treeNode(1000000, treeNode(2000000), treeNode(3000000))
        tree_b = treeNode(999999, treeNode(2000000), treeNode(3000000))
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_deep_tree(self):
        """Test deeply nested tree"""
        # Create chain: 1 -> 2 -> 3 -> ... -> 10
        tree_a = treeNode(1)
        current = tree_a
        for i in range(2, 11):
            current.left = treeNode(i)
            current = current.left
        
        # Create chain: 0 -> 1 -> 2 -> ... -> 10
        tree_b = treeNode(0)
        current = tree_b
        for i in range(1, 11):
            current.left = treeNode(i)
            current = current.left
        
        self.assertTrue(are_leaf_similar(tree_a, tree_b))

    def test_left_vs_right_child_position(self):
        """Test that leaf position in tree doesn't matter, only sequence"""
        #       1             1
        #      /             / \
        #     2             2   3
        tree_a = treeNode(1, treeNode(2))
        tree_b = treeNode(1, treeNode(2), treeNode(3))
        self.assertFalse(are_leaf_similar(tree_a, tree_b))


if __name__ == "__main__":
    unittest.main()
