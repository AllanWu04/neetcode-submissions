class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = 0
        sell_price = 1
        max_profit = 0

        while sell_price < len(prices):
            profit = prices[sell_price] - prices[buy_price]
            if profit < 0: #Then our curr buy price is > curr sell price, move buy price to right
                buy_price = sell_price
            else:
                max_profit = max(profit, max_profit)
            sell_price += 1

        return max_profit
