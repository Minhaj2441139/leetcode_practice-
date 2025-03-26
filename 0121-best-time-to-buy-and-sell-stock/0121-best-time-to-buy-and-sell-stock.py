class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0

        for p in prices[1:]:
            cost=p-mini
            profit=max(profit,cost)
            mini=min(p,mini)
        
        return profit
        
        