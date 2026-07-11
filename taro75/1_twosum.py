import unittest


def twosum(nums: list[int], target: int) -> tuple[int, int]:
    no_solution = (-1, -1)
    index_map = {}
    for index, num in enumerate(nums):
        wanted_number = target - num
        if wanted_number in index_map:
            return (index_map[wanted_number], index)
        index_map[num] = index
    return no_solution


class TwoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        nums = [-5, -1, 0, 0, 2, 2, 3]
        target = -2
        answer = twosum(nums, target)
        expected = (0, 6)
        self.assertEqual(answer, expected)

    def test_no_solution(self):
        nums = [-5, -1, 0, 0, 2, 2, 3]
        target = 99
        answer = twosum(nums, target)
        expected = (-1, -1)
        self.assertEqual(answer, expected)

    def test_empty_list(self):
        nums = []
        target = -2
        answer = twosum(nums, target)
        expected = (-1, -1)
        self.assertEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()
