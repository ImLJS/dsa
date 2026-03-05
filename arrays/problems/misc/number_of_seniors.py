# 2678. Number of Senior Citizens - Easy

# Link: https://leetcode.com/problems/number-of-senior-citizens/

# Given a 0-indexed array of strings details, where each details[i] consists of a space-separated string of the form "name age city", return the number of senior citizens. A senior citizen is defined as a person whose age is greater than 60.

# Example 1:
# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The details of the people are:
# "7868190130M7522" -> age is 75, so this person is a senior citizen.
# "5303914400F9211" -> age is 92, so this person is a senior citizen.
# "9273338290F4010" -> age is 40, so this person is not a senior citizen.
# There are 2 senior citizens, so we return 2.

# Note:
# 1. 1 <= details.length <= 100
# 2. details[i].length == 15
# 3. details[i] consists of digits and uppercase English letters.

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_count = 0
        
        for detail in details:
            age = int(detail[11:13])  # Extract the age from the string
            if age > 60:
                senior_count += 1
        
        return senior_count

# Notes:
# 1. We initialize a variable `senior_count` to keep track of the number of senior citizens.
# 2. We iterate through each string in the input array `details`. For each string, we extract the age by slicing the string from index 11 to 13 and converting it to an integer.
# 3. We check if the extracted age is greater than 60. If it is, we increment the `senior_count` by 1.
# 4. Finally, we return the total count of senior citizens.

# Time Complexity: O(n), where n is the length of the input array `details`, as we need to iterate through each string once.
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the count of senior citizens.