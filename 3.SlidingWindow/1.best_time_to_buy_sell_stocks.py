"""
Buy and Sell Crypto
Solved 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Input: prices = [10,1,5,6,7,1]

Output: 6
"""

prices = [5, 1, 5, 6, 7, 1]

# expected 6

max_prof = 0
l = 0
r = 1
while r < len(prices):
    profit = prices[r] - prices[l]
    if profit <= 0:
        l = r
        r += 1
    if profit > 0:
        r += 1
    max_prof = max(profit, max_prof)
print(max_prof)
