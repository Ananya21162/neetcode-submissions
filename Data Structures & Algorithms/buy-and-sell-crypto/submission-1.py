class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxP = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice
            if profit >0:
                maxP = max(maxP,profit)
        return maxP
        