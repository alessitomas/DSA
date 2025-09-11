from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        self.window.append(val)
        
        while len(self.window) > self.size:
            self.total -= self.window.popleft()

        return self.total / len(self.window)        



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)