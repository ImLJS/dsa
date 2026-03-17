"""
Problem: Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

def max_profit(prices):
    """
    Calculate the maximum profit from a single buy-sell transaction.

    :param prices: List[int] - List of stock prices
    :return: int - Maximum profit achievable
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Notes:

# The algorithm iterates through the list of prices while keeping track of the minimum price encountered so far.
# For each price, it calculates the potential profit by subtracting the minimum price from the current price.
# If the calculated profit is greater than the current maximum profit, it updates the maximum profit.

# Time Complexity: O(n)
# - We iterate through the prices array once, where n is the length of the array.
# - Each operation inside the loop is O(1).
# Therefore, the overall time complexity is O(n).

# Space Complexity: O(1)
# - We use only two variables (min_price and max_profit) to store intermediate results.
# - No additional data structures are used.
# Therefore, the space complexity is O(1).