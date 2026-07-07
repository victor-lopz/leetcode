/* You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length */

import java.util.Deque;
import java.util.ArrayDeque;

public class maxSlidingWindow {
    static int[] maxWindows(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 1 || k > nums.length) {
            return new int[] {};
        }
        int[] maximums = new int[nums.length-k+1];
        Deque<Integer> q = new ArrayDeque<Integer>();
        for (int i = 0; i < k; ++i) {
            while (!q.isEmpty() && nums[i] >= nums[q.peekLast()]) {
                q.removeLast();
            }
            q.addLast(i);
        }
        for (int i = 0; i < maximums.length - 1; ++i) {
            maximums[i] = nums[q.peekFirst()];
            if (q.peekFirst() == i) {
                q.removeFirst();
            }
            while (!q.isEmpty() && nums[i+k] >= nums[q.peekLast()]) {
                q.removeLast();
            }
            q.addLast(i+k);
        }
        maximums[maximums.length - 1] = nums[q.peekFirst()];
        return maximums;
    }
    public static void main(String[] args) {
        int[] nums = new int[] {1,3,-1,-3,-2,-4,5,3,-4,-5,-3,-1,-2,2,6,-1,-3};
        int k = 3;
        int[] ans = maxWindows(nums, k);
        for (int x : ans) {
            System.out.print(x + " ");
        }
    }
}

