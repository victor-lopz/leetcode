import unittest

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged_intervals = []
    if not intervals:
        return merged_intervals
    def start_of_interval(interval: list[int]) -> int:
        return interval[0]
    
    intervals = sorted(intervals, key=start_of_interval)
    previous_end = - float('inf')
    for current_interval in intervals:
        current_start, current_end = current_interval
        if previous_end < current_start: # No overlapping
            merged_intervals.append(current_interval)
            previous_end = current_end
        else: # There is overlapping
            if current_end > previous_end: # select largest end for merged interval
                previous_end = current_end 
            merged_intervals[-1][1] = previous_end
    return merged_intervals

class mergeIntervalsTestCase(unittest.TestCase):
    
    def test_overlapping(self) -> None:
        intervals = [[3,4], [2,3]]
        expected = [[2,4]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)

    def test_non_overlapping(self) -> None:
        intervals = [[3,4], [2,2]]
        expected = [[2,2], [3,4]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)
        
    def test_empty(self) -> None:
        intervals = []
        expected = []
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)
        
    def test_None(self) -> None:
        intervals = None
        expected = []
        merged_intervals = merge_intervals(intervals) # type: ignore
        self.assertEqual(expected, merged_intervals)
        
    def test_many_intervals(self) -> None:
        intervals = [[1,7], [2,3], [3,5], [4,8], [8,9], [10,12]]
        expected = [[1,9], [10,12]]
        merged_intervals = merge_intervals(intervals)
        self.assertEqual(expected, merged_intervals)

if __name__ == "__main__":
    unittest.main()