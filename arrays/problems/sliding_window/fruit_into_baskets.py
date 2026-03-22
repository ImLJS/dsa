"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

1. You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
2. Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the starting tree) while moving to the right. The picked fruits must fit in one of your baskets.
3. Once you reach a tree with a fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the maximum number of fruits you can pick.

Example:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2]. If we had started at the first tree, we would only pick from trees [0,1].

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

def total_fruit(fruits):
    """
    Sliding Window Approach to solve the problem.

    :param fruits: List[int] - List of integers representing fruit types.
    :return: int - Maximum number of fruits that can be picked.
    """
    # Initialize variables
    max_fruits = 0
    basket = {}
    left = 0

    # Iterate through the array
    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1

        # If we have more than 2 types of fruits, shrink the window
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        # Update the maximum number of fruits
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

# Note:

# The function `total_fruit` implements the sliding window technique to find the longest contiguous subarray that contains at most two distinct integers (fruit types). It uses a dictionary to keep track of the count of each fruit type in the current window. When the number of distinct fruit types exceeds two, it shrinks the window from the left until it is valid again. The maximum length of a valid window is updated throughout the iteration. 

# The time complexity of this solution is O(n) where n is the length of the input array, and the space complexity is O(1) since the dictionary will hold at most 2 entries.
# Space complexity is O(1) because the dictionary will hold at most 2 entries, regardless of the input size.