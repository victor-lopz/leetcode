def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2:
        return s
    start, end = 0, 0

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right

    for center in range(len(s)):
        odd_left, odd_right = expand(left=center, right=center)
        if odd_right - odd_left > end - start:
            start, end = odd_left, odd_right
        even_left, even_right = expand(left=center, right=center + 1)
        if even_right - even_left > end - start:
            start, end = even_left, even_right
    return s[start:end]


def main() -> None:
    result = longest_palindromic_substring("ababaab")
    assert result == "ababa"

    result2 = longest_palindromic_substring("ababaababa")
    assert result2 == "ababaababa"

    two_char = longest_palindromic_substring("ab")
    assert two_char == "a"


if __name__ == "__main__":
    main()
