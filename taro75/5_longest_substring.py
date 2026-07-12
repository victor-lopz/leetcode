import unittest


def longest_substring_without_duplicates(s: str) -> int:
    """
    Find the length of the longest substring
    without repeating characters.

    Time complexity: O(n), where n = len(s).
    Space complexity: O(min(n, d)),
    where d is the number of distinct characters in s.

    Args:
        s: Input string.

    Returns:
        Length of longest substring without duplicates.

    Examples:
        >>> longest_substring_without_duplicates("asda")
        3
        >>> longest_substring_without_duplicates("qwertywwerty")
        6
    """

    char_index: dict[str, int] = {}  # Maps char -> most recent index
    max_length = 0
    left = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length


class LongestSubstringTestCase(unittest.TestCase):
    def test_empty_string(self) -> None:
        self.assertEqual(0, longest_substring_without_duplicates(""))

    def test_all_identical_characters(self) -> None:
        self.assertEqual(1, longest_substring_without_duplicates("hhhhhhhhhhhhh"))

    def test_all_unique_characters(self) -> None:
        self.assertEqual(16, longest_substring_without_duplicates("qwerty1234567890"))

    def test_alternating_duplicates(self) -> None:
        self.assertEqual(
            3, longest_substring_without_duplicates("asdasdsaddasdasdsadasdsas")
        )

    def test_duplicate_at_boundary(self) -> None:
        self.assertEqual(6, longest_substring_without_duplicates("qwertywwerty"))

    def test_repeated_cycles_of_unique_characters(self) -> None:
        unique_characters = (
            "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        )
        repeated_input = unique_characters * 10
        self.assertEqual(62, longest_substring_without_duplicates(repeated_input))


if __name__ == "__main__":
    unittest.main()
