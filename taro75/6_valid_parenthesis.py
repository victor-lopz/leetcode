import unittest


def is_valid(parentheses_string: str) -> bool:
    """
    Checks if a string containing parentheses is valid.

    Time complexity: O(n), where n = len(parentheses_string).
    Space complexity: O(n), due to storing open brackets in stack.

    Args:
        parentheses_string: String containing only '(', ')', '[', ']', '{', '}'

    Returns:
        True if valid, False otherwise.
    """
    if len(parentheses_string) % 2:
        return False
    stack = []
    open_to_close = {"(": ")", "{": "}", "[": "]"}
    for char in parentheses_string:
        if char in open_to_close:
            stack.append(char)
        elif not stack or open_to_close[stack.pop()] != char:
            return False
    return not stack


class IsValidTestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_valid("()"))

    def test_2(self):
        self.assertTrue(is_valid("()[]{}"))

    def test_3(self):
        self.assertFalse(is_valid("(]"))

    def test_4(self):
        self.assertTrue(is_valid("([])"))

    def test_5(self):
        self.assertFalse(is_valid("([)]"))

    def test_valid(self):
        self.assertTrue(is_valid("[(){}]{[()]}"))

    def test_not_valid(self):
        self.assertFalse(is_valid("[(])"))

    def test_not_valid2(self):
        self.assertFalse(is_valid("["))

    def test_empty_str(self):
        self.assertTrue(is_valid(""))


if __name__ == "__main__":
    unittest.main()
