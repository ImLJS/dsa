# 387. First Unique Character in a String - Easy

# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string s, return the index of the first non-repeating character in it.
# If it does not exist, return -1.

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Return index of first non-repeating character or -1 if none.

        Time: O(n)
        Space: O(1) (constant 26 letters) or O(n) in general
        """
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ]
    for s, expected in tests:
        out = sol.firstUniqChar(s)
        print(f"{s!r} -> {out} (expected {expected})")

# Notes

# 1. We use the `Counter` class from the `collections` module to count the frequency of each character in the string `s`.
# 2. We iterate through the string `s` using `enumerate` to get both the index and the character. For each character, we check if its count in the `Counter` is 1, which means it is a non-repeating character.
# 3. If we find a non-repeating character, we return its index. If we finish iterating through the string without finding any non-repeating character, we return -1.

# Time Complexity: O(n) - We iterate through the string once to count the characters and once to find the first unique character.
# Space Complexity: O(1) - The `Counter` will at most store 26 characters (since the problem states that the string consists of lowercase English letters), which is a constant amount of space. In general, if the string can contain any characters, the space complexity would be O(n) in the worst case.
