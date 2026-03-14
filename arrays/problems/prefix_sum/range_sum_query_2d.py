# 304. Range Sum Query 2D - Immutable - Medium

# Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

# Given a 2D matrix matrix, handle multiple queries of the following type:
# - Calculate the sum of the elements of matrix inside the rectangle defined by
#   its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:
# - NumMatrix(int[][] matrix) initializes the object with the integer matrix matrix.
# - int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the
#   elements of matrix inside the rectangle defined by its upper left corner
#   (row1, col1) and lower right corner (row2, col2).

# Example 1:
# Input: ["NumMatrix","sumRegion","sumRegion","sumRegion"], [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
# Output: [null, 8, 11, 12]

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.prefix[i][j] = self.prefix[i-1][j]+self.prefix[i][j-1]-self.prefix[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        preBottomRight = self.prefix[row2+1][col2+1]
        preTopRight = self.prefix[row1][col2+1]
        preBottomLeft = self.prefix[row2+1][col1]
        preTopLeft = self.prefix[row1][col1]
        return preBottomRight-preTopRight-preBottomLeft+preTopLeft

# Notes:
# 1. Similar to the 1D case, we can use a 2D prefix sum array to store the cumulative sums of the input matrix.
# 2. The prefix sum array allows us to calculate the sum of any rectangular region in O(1) time by using the inclusion-exclusion principle.
# 3. The space complexity of this solution is O(m*n) due to the prefix sum array, where m and n are the dimensions of the input matrix, and the time complexity for each sumRegion query is O(1).

# Pattern: Prefix Sum
# Time:  O(m*n) build, O(1) query
# Space: O(m*n)
