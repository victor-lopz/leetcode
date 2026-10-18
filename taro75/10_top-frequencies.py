from collections import Counter


def top_k_elements(array: list[int], k: int) -> list[int]:
    if k <= 0 or not array:
        return []
    counter = Counter(array)
    bucket: list[list[int]] = [[] for _ in range(len(array) + 1)]
    for num, freq in counter.items():
        bucket[freq].append(num)
    top_k_nums: list[int] = []
    for freq in range(len(array), 0, -1):
        for num in bucket[freq]:
            top_k_nums.append(num)
            if len(top_k_nums) == k:
                return top_k_nums
    return top_k_nums


def main() -> None:
    result = top_k_elements([5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 3, -654, -654], k=5)
    assert result == [7, 5, -654, 3]

    empty = top_k_elements([], k=5)
    assert empty == []

    empty2 = top_k_elements([321321546, 6543354], k=0)
    assert empty2 == []

    one = top_k_elements([3, 6], k=1)
    assert one == [3] or one == [6]

    result3 = top_k_elements([5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 3, -654, -654], k=3)
    assert result3 == [7, 5, -654]


if __name__ == "__main__":
    main()
