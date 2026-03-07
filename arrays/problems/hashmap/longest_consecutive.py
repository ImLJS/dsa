# 128. Longest Consecutive Sequence - Medium

# Link: https://leetcode.com/problems/longest-consecutive-sequence/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Notes:
# - We use a set to store the numbers for O(1) lookups.
# - We iterate through each number in the set, and if it's the start of a sequence (i.e., num - 1 is not in the set), we count how long the sequence is by checking for consecutive numbers until we can't find the next one.
# - We keep track of the longest streak found and return it at the end.

# Time Complexity: O(n) - We traverse the list of numbers once to create the set, and then we potentially traverse the longest consecutive sequence once for each number in the set.
# Space Complexity: O(n) - We use a set to store the unique numbers from the input list.
