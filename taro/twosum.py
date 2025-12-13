def twosum(nums: list[int], target: int) -> tuple[int, int]:
    no_solution = (-1,-1)
    index_of = {}
    for index, num in enumerate(nums):
        looking_for = target - num
        if looking_for in index_of:
            return (index_of[looking_for], index)
        index_of[num] = index
    return no_solution

def test():
    nums = [-5,-1,0,0,2,2,3]
    target = -2
    answer = twosum(nums, target)
    print(f"{answer = }")
    expected = [0,6]
    
test()
