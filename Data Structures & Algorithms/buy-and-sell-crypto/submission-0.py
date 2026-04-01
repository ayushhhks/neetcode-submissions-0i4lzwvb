class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=0
        profit=0
        max_profit=0
        length=len(prices)
        for i in range(length):
            for j in range(i+1,length,1):
                buy=prices[i]
                sell=prices[j]
                if sell>buy:
                 profit=sell-buy
                 max_profit=max(max_profit, profit)

                elif sell<buy:
                 continue

           

            
        return max_profit


            
