'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(prices):
    
    #brute force time complexity O(n^2)
    max_profit = 0
    # for i in range(len(prices)):
    #     buy = i
    #     for j in range(i, len(prices)):
    #         if i > j:
    #             max_profit = max(max_profit, (j-i))
    # return max_profit
    
    #let's use two pointer left and right pointer 
    
    left = 0
    right = 1
    max_profit = 0
    curren_profit =0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            curren_profit = prices[right] - prices[left]
            max_profit = max(max_profit, curren_profit)
        else:
            left = right
        right += 1
    return max_profit
    
        
            



prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
print(maxProfit(prices))