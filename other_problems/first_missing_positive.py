# 41. First Missing Positive
# Hard
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] < 0:
            nums[i] = 0
    for i in range(n):
        current_number = abs(nums[i])
        if 0 < current_number <= n:
            target_index = current_number - 1
            if nums[target_index] == 0:
                nums[target_index] = -(n + 1)
            elif nums[target_index] > 0:
                nums[target_index] = -nums[target_index]
    for i in range(n):
        if nums[i] >= 0:
            return i + 1
    return n + 1


def main() -> None:
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    long_array = [-1 for _ in range(1000000)]
    assert first_missing_positive(long_array) == 1
    long_array2 = [0 for _ in range(1000000)]
    assert first_missing_positive(long_array2) == 1
    long_array3 = [i for i in range(1000000)]
    assert first_missing_positive(long_array3) == 1000000


main()


# Input: nums = [3,4,-1,1]
# swap 3 with -1
# [-1,4,3,1]
# swap 4 with 1
# [-1,1,3,4]
# swap 1 and -1
# [1,-1,3,4]
