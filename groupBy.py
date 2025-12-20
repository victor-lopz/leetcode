from collections import defaultdict
from typing import TypeVar, Callable, Sequence, Optional

T = TypeVar("T")
K = TypeVar("K")

def groupBy(array: Sequence[T], 
            key_func: Callable[[T], K]
            ) -> dict[K, list[T]]:
    """
    Groups array elements by the result of key_func.
    
    Args:
        array: Sequence of elements to group
        key_func: Custom function that outputs they grouping key for each element
    
    Returns:
        Dictionary mapping each output of key_func to a list of 
        elements that achieve it.
    
    Examples:
        >>> groupBy(["a", "A", "b", "A"], str.islower)
        {"true": ["a", "b"], "false": ["A", "A"]}
        
        >>> groupBy(['a', 'A', 'b', 'A', 'B'], str.lower)
        {'a': ['a', 'A', 'A'], 'b': ['b', 'B']}
    """
    if not key_func:
        raise ValueError("Custom function cannot be None.")
    if not array or not len(array):
        return {}
    grouped = defaultdict(list)
    for element in array:
        key = key_func(element)
        grouped[key].append(element)
    return dict(grouped)

def groupCount(array: list[T], 
               key_func: Callable[[T], K] = lambda x:x
               ) -> dict[K, int]:
    """
    Counts the number of unique outputs from key_func. 
    If key_func is not provided, then counts the number of unique elements.
    Args:
        array: Sequence of elements
        key_func: Custom function to extract the counting key
    Returns:
        Dictionary mapping each key to its number of ocurrences.
    Examples:
        >>> groupCount([3, 3, 3, 2, 2, 1])
        {3:3, 2:2, 1:1}
        >>> groupCount([3, 3, 3, 2, 2, 1], int.bitlength)
        {2:5, 1:1}
    """
    if not array or not len(array):
        return {}
    grouped = defaultdict(int)
    for element in array:
        key = key_func(element)
        grouped[key] += 1
    return dict(grouped)

def groupStringsByIsLowerTestCase() -> None:
    array = ['a', 'a', 'b', 'A', 'A', 'BB']
    groups = groupBy(array, str.islower)
    print(f"{groups = }")

def groupStringsByLowerTestCase() -> None:
    array = ['a', 'A', 'b', 'B']   
    groups = groupBy(array, str.lower)
    print(f"{groups = }")

def groupCountIntegersTestCase() -> None:
    array = [1, 7, 1, 5, 7, 7, 3]
    counts = groupCount(array)
    print(f"{counts = }")

def groupCountIntegersByBitLengthTestCase() -> None:
    array = [3, 3, 3, 2, 2, 1]
    counts = groupCount(array, int.bit_length)
    print(f"{counts = }")

if __name__ == "__main__":
    groupStringsByIsLowerTestCase()
    groupStringsByLowerTestCase()
    groupCountIntegersTestCase()
    groupCountIntegersByBitLengthTestCase()