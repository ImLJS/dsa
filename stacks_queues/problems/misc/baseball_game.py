# 682. Baseball Game - Easy

# Link: https://leetcode.com/problems/baseball-game/

# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores. At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
# 1. An integer x - Record a new score of x.

# 2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.

# 3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.

# 4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

# Return the sum of all the scores on the record after applying all the operations.

# Example 1:
# Input: ops = ["5","2","C","D","+"]
# Output: 30

# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Example 2:
# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27

# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

# Constraints:
# 1 <= ops.length <= 1000
# ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].

from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for op in ops:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        return sum(record)
    
# Notes

# 1. We use a list `record` to keep track of the scores for each round.
# 2. We iterate through each operation in `ops` and perform the corresponding action based on the type of operation:
#    - If the operation is "C", we remove the last score from `record`.
#    - If the operation is "D", we calculate double the last score and append it to `record`.
#    - If the operation is "+", we calculate the sum of the last two scores and append it to `record`.
#    - If the operation is an integer, we convert it to an integer and append it to `record`.
# 3. Finally, we return the sum of all the scores in `record` as the final result.

# Time Complexity: O(n) - We iterate through the list of operations once.
# Space Complexity: O(n) - In the worst case, we may store all scores in the `record` list.
