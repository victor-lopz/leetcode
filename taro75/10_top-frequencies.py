from collections import defaultdict
import heapq


def top_k_elements(array: list[int], k: int) -> list[int]:
    counter = defaultdict(int)
    for num in array:
        counter[num] += 1
    frequencies = [(freq, num) for num, freq in counter.items()]
    heapq.heapify_max(frequencies)
    top_k_nums = []
    for i in range(min(k, len(frequencies))):
        _top_i_freq, top_i_num = heapq.heappop_max(frequencies)
        top_k_nums.append(top_i_num)
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


if __name__ == "__main__":
    main()
