def expand(s: str, left: int, right: int) -> tuple[int, int]:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right


def get_palindrome(s: str, center: int) -> tuple[int, int]:
    odd_left, odd_right = expand(s, left=center, right=center)
    even_left, even_right = expand(s, left=center, right=center + 1)
    if odd_right - odd_left > even_right - even_left:
        return odd_left, odd_right
    return even_left, even_right


def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2:
        return s
    start, end = 0, 0
    for center in range(len(s)):
        left, right = get_palindrome(s, center)
        if right - left > end - start:
            start, end = left, right
    return s[start:end]


def main() -> None:
    result = longest_palindromic_substring("ababaab")
    print(result)
    assert result == "ababa"

    result2 = longest_palindromic_substring("ababaababa")
    assert result2 == "ababaababa"

    two_char = longest_palindromic_substring("ab")
    assert two_char == "a"


if __name__ == "__main__":
    main()
