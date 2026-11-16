class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxp = 0
        while r <len(prices):
            if prices[r]-prices[l] >0:
                maxp = max(prices[r]-prices[l], maxp)
            else:
                l = r
            r +=1
        return maxp