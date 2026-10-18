def find_duplicates(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            target_index = nums[i] - 1
            nums[i], nums[target_index] = nums[target_index], nums[i]
    duplicates = []
    for i in range(n):
        if nums[i] != i + 1:
            duplicates.append(nums[i])
    return duplicates


def main() -> None:
    assert find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) in [[3, 2], [2, 3]]


main()
