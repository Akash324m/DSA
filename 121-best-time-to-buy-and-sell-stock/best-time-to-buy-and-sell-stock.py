class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = prices[0]
        # bday=0
        # for x in range(len(prices)):
        #     if buy > prices[x]:
        #         buy = prices[x]
        #         bday = x
        # if bday == (len(prices)-1):
        #     return 0
        # sell = prices[bday+1]
        # sday=0
        # for y in range(bday+1, len(prices)):
        #     if sell<prices[y]:
        #         sell=prices[y]
        #         sday=y
        # return sell-buy
        # profit=0
        # sell=0
        # buy=0
        # for x in range(len(prices)):
        #     for y in range(len(prices)):
        #         if profit<(sell-buy)
        maxp=0
        min_price = prices[0]
        for p in prices[1:]:
            current = p - min_price
            maxp = max(maxp,current)
            min_price = min(min_price,p)
        return maxp

