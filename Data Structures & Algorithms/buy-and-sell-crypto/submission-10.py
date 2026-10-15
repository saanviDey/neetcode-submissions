class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = l + 1

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
        
        return max_profit
        

        