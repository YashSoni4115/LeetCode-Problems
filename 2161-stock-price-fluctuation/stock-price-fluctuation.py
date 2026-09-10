import heapq

class StockPrice:

    def __init__(self):
        self.prices = {}
        self.currTime = 0
        self.minheap = []
        self.maxheap = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.currTime = max(self.currTime, timestamp)

        heapq.heappush(self.minheap, (price, timestamp))
        heapq.heappush(self.maxheap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.currTime]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxheap[0]
            price = -price
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.maxheap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minheap[0]
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.minheap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()