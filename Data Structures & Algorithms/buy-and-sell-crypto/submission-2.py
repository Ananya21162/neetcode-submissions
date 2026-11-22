class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy at min & sell at max
        BP, SP, profit = prices[0], 0, 0
        for i in range(1, len(prices)):
            if prices[i]-BP > 0:
                profit = max (profit,prices[i]-BP )

            BP = min(BP, prices[i])
        return profit

      