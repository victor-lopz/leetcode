from collections import defaultdict
import collections.abc
from typing import TypeVar, Callable, Iterable, Hashable
import unittest

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)

__all__ = ["group_by", "group_count"]


def group_by(array: Iterable[T], key_func: Callable[[T], K]) -> dict[K, list[T]]:
    """
    Groups array elements by the result of key_func.

    Args:
        array: Iterator of elements to group. Can be a list, tuple, set, dict...
        key_func: Custom function that outputs the grouping key for each element

    Returns:
        Dictionary mapping each output of key_func to a list of
        elements that achieve it.

    Examples:
        >>> group_by(["a", "A", "b", "A"], str.islower)
        {True: ["a", "b"], False: ["A", "A"]}

        >>> group_by(['a', 'A', 'b', 'A', 'B'], str.lower)
        {'a': ['a', 'A', 'A'], 'b': ['b', 'B']}
    """
    if not isinstance(array, collections.abc.Iterable):
        raise TypeError("Input parameter 'array' must be an iterable.")
    if not callable(key_func):
        raise TypeError("Input parameter 'key_func' must be of type callable.")
    grouped = defaultdict(list)
    for element in array:
        try:
            key = key_func(element)
        except Exception as e:
            raise ValueError(f"key_func failed on element {element}: {e}") from e
        grouped[key].append(element)
    return dict(grouped)


def group_count(
    array: Iterable[T], key_func: Callable[[T], K] = lambda x: x
) -> dict[K, int]:
    """
    Counts the number of unique outputs from key_func.
    If key_func is not provided, then counts the number of unique elements.
    Args:
        array: Iterator of elements. Can be a list, tuple, set, dict...
        key_func: Custom function to extract the counting key
    Returns:
        Dictionary mapping each key to its number of occurrences.
    Examples:
        >>> group_count( [3, 3, 3, 2, 2, 1] )
        {3:3, 2:2, 1:1}
        >>> group_count( (3, 3, 3, 2, 2, 1) , int.bit_length)
        {2:5, 1:1}
    """
    if not isinstance(array, collections.abc.Iterable):
        raise TypeError("Input parameter 'array' must be an iterable.")
    if not callable(key_func):
        raise TypeError("Input parameter 'key_func' must be of type callable.")
    grouped = defaultdict(int)
    for element in array:
        try:
            key = key_func(element)
        except Exception as e:
            raise ValueError(f"key_func failed on element {element}: {e}") from e
        grouped[key] += 1
    return dict(grouped)


class GroupByTestCase(unittest.TestCase):
    def test_group_by_is_lower(self) -> None:
        array = ["a", "a", "b", "A", "A", "B"]
        is_lower_groups = group_by(array, str.islower)
        expected = {True: ["a", "a", "b"], False: ["A", "A", "B"]}
        self.assertEqual(is_lower_groups, expected)

    def test_group_by_lower(self) -> None:
        array = ["a", "a", "b", "A", "A", "B"]
        lower_groups = group_by(array, str.lower)
        expected = {"a": ["a", "a", "A", "A"], "b": ["b", "B"]}
        self.assertEqual(lower_groups, expected)

    def test_group_by_null_array(self) -> None:
        self.assertRaises(TypeError, group_by, None, str.islower)

    def test_group_by_empty_array(self) -> None:
        empty_array = []
        is_lower_groups = group_by(empty_array, str.islower)
        expected = {}
        self.assertEqual(is_lower_groups, expected)

    def test_group_by_non_callable(self) -> None:
        array = [3, 2, 1]
        self.assertRaises(TypeError, group_by, array, 2)

    def test_group_by_key_func_value_error(self) -> None:
        array_of_ints = [1, 2, 3]
        self.assertRaises(ValueError, group_by, array_of_ints, str.lower)

    def test_group_by_with_generator(self) -> None:
        call_count = 0

        def number_generator():
            nonlocal call_count
            call_count += 1
            yield 1
            yield 2
            yield 1
            yield 3

        group_by_parity = group_by(number_generator(), lambda x: x % 2)
        expected = {1: [1, 1, 3], 0: [2]}
        self.assertEqual(expected, group_by_parity)
        self.assertEqual(call_count, 1)


class GroupCountTestCase(unittest.TestCase):
    def test_group_count_ints(self) -> None:
        integer_tuple = (3, 3, 3, 3, 2, 2, 1)
        counts = group_count(integer_tuple)
        expected = {3: 4, 2: 2, 1: 1}
        self.assertEqual(counts, expected)

    def test_group_count_ints_by_bit_length(self) -> None:
        integer_tuple = (3, 3, 3, 3, 2, 2, 1)
        bit_counts = group_count(integer_tuple, int.bit_length)
        expected = {2: 6, 1: 1}
        self.assertEqual(bit_counts, expected)

    def test_group_count_null(self) -> None:
        self.assertRaises(TypeError, group_count, None, str.lower)

    def test_group_count_non_callable(self) -> None:
        self.assertRaises(TypeError, group_count, [], 2)

    def test_group_count_empty_array(self) -> None:
        self.assertEqual({}, group_count([], str.upper))

    def test_group_count_several_types(self) -> None:
        counts = group_count([5, "a"])
        expected = {5: 1, "a": 1}
        self.assertEqual(expected, counts)

    def test_group_by_unhashable_key(self) -> None:
        # key_func returns a list (unhashable)
        self.assertRaises(TypeError, group_count, [1, 2], lambda x: [x])

    def test_group_count_with_generator(self) -> None:
        call_count = 0

        def number_generator():
            nonlocal call_count
            call_count += 1
            yield 1
            yield 2
            yield 1
            yield 3

        group_by_parity = group_count(number_generator(), lambda x: x % 2)
        expected = {1: 3, 0: 1}
        self.assertEqual(expected, group_by_parity)
        self.assertEqual(call_count, 1)


if __name__ == "__main__":
    unittest.main()
