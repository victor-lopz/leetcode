import unittest


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current_start, current_end in intervals[1:]:
        previous_start, previous_end = merged[-1]
        if previous_end >= current_start:  # Overlap
            merged[-1] = [previous_start, max(previous_end, current_end)]
        else:
            merged.append([current_start, current_end])
    return merged


class MergeIntervalsTestCase(unittest.TestCase):
    def test_overlapping(self) -> None:
        intervals = [[3, 4], [2, 3]]
        expected = [[2, 4]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)

    def test_non_overlapping(self) -> None:
        intervals = [[3, 4], [2, 2]]
        expected = [[2, 2], [3, 4]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)

    def test_empty(self) -> None:
        intervals = []
        expected = []
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)

    def test_many_intervals(self) -> None:
        intervals = [[1, 7], [2, 3], [3, 5], [4, 8], [8, 9], [10, 12]]
        expected = [[1, 9], [10, 12]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)


if __name__ == "__main__":
    unittest.main()
