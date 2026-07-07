import unittest


def flatten(nested_list: list[list], max_depth=None) -> tuple[list, int]:
    """
    Flattens and computes the level of nesting of a given nested array.
    Optionally, if max_depth is given, stops de-nesting at that level of depth.
    Example: flatten( [0, [7, [2, 5], 3], 9] , max_depth = 1 ) = ( [0, 7, [2, 5], 3, 9] ,  1)

    :param nested_list: Array that may or may not contain nested arrays
    :type nested_list: list[Any | list[...]]
    :param max_depth: Optional parameter to specify how many orders of nesting to undo.
                    By default, everything is unested.
    :type max_depth: int|None
    :return: Tuple containing the flattened array and its nesting depth.
    :rtype: tuple[list, int]
    """
    if max_depth == 0:
        return nested_list, 0
    flattened = []
    if not max_depth:
        max_depth = float("inf")
    nesting_depth = 0

    def recursive_flattener(
        nested_array: list, output: list, current_depth: int
    ) -> None:
        nonlocal nesting_depth
        depth_anotated = False
        for element in nested_array:
            if isinstance(element, list) and current_depth < max_depth:
                if not depth_anotated:
                    nesting_depth += 1
                    depth_anotated = True
                recursive_flattener(element, output, current_depth + 1)
            else:
                output.append(element)

    recursive_flattener(nested_list, flattened, 0)
    return flattened, nesting_depth


class ArrayFlattenerTestCase(unittest.TestCase):
    def test_example_nested_array_int(self):
        nested_array = [0, [7, [2, 5], 3], 9]
        max_depth = 1
        expected = [0, 7, [2, 5], 3, 9]
        flat_array, depth = flatten(nested_array, max_depth)
        self.assertEqual(flat_array, expected)
        self.assertEqual(depth, max_depth)

    def test_nested_array_int1(self):
        nested_array = [
            [],
            0,
            1,
            [
                2,
                3,
                [4, [], 5],
                [],
            ],
            [6],
        ]
        expected = [0, 1, 2, 3, 4, 5, 6]
        flat_array, depth = flatten(nested_array, 3)
        self.assertEqual(flat_array, expected)
        self.assertEqual(depth, 3)

    def test_nested_array_int2(self):
        nested_array = [0, 1, [2, 3, [4, 5]], [6]]
        expected = [0, 1, 2, 3, 4, 5, 6]
        flat_array, depth = flatten(nested_array)
        self.assertEqual(flat_array, expected)
        self.assertEqual(depth, 2)

    def test_empty_array(self):
        empty_array = []
        flat_array, depth = flatten(empty_array)
        self.assertEqual(empty_array, flat_array)
        self.assertEqual(depth, 0)

    def test_nested_array_str(self):
        nested_array = ["s", "", ["kk", [[[[["h"]]]]]], "djgv"]
        expected = ["s", "", "kk", "h", "djgv"]
        flat_array, depth = flatten(nested_array, 6)
        self.assertEqual(flat_array, expected)
        self.assertEqual(depth, 6)


if __name__ == "__main__":
    unittest.main()
