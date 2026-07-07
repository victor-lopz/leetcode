def twosum(nums: list[int], target: int) -> tuple[int, int]:
    no_solution = (-1, -1)
    index_map = {}
    for index, num in enumerate(nums):
        wanted_number = target - num
        if wanted_number in index_map:
            return (index_map[wanted_number], index)
        index_map[num] = index
    return no_solution


def test1():
    nums = [-5, -1, 0, 0, 2, 2, 3]
    target = -2
    answer = twosum(nums, target)
    expected = (0, 6)
    print(f"{answer = }, {expected = }")


def test2_no_answer():
    nums = [-5, -1, 0, 0, 2, 2, 3]
    target = 99
    answer = twosum(nums, target)
    expected = (-1, -1)
    print(f"{answer = }, {expected = }")


def test3_empty():
    nums = []
    target = -2
    answer = twosum(nums, target)
    expected = (-1, -1)
    print(f"{answer = }, {expected = }")


test1()
test2_no_answer()
test3_empty()
