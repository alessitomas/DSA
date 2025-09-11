"""

["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]


{"foo": 1 "bar": 2}

[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
        T            T             F        F.           F              T  


1 -> t + 10

cur >= t + 10: true and update last print
false


"""

from collections import deque
class Logger:
        
    # S: O(N), where N is the number of unique messages 
    def __init__(self): 
        self.msg_queue = deque()
        self.msg_set = set()
        self.TIMEOUT = 10

    def clean_up(self, curr_timestamp):
        while len(self.msg_queue) > 0 and curr_timestamp - self.msg_queue[0][1] >= self.TIMEOUT:          
            message, _ = self.msg_queue.popleft()
            self.msg_set.remove(message)

    # t: O(1)
    # s: O(1)
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        self.clean_up(timestamp)
        
        if message in self.msg_set:
            return False

        
        self.msg_queue.append((message, timestamp))
        self.msg_set.add(message)
        return True
        
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)