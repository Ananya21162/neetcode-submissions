class StockSpanner:

    def __init__(self):
        self.stock = []
        self.prices = []
        
    def next(self, price: int) -> int:
        self.prices.append(price)
        while self.stock and self.stock[-1][0] <= price:
            top = self.stock[-1][0]
            if top <= price:
                self.stock.pop()
       
        if not self.stock:
            ans = len(self.prices)
        else:
            ans = len(self.prices)-1 - self.stock[-1][1]
        self.stock.append((price,len(self.prices)-1))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)