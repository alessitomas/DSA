"""

["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]


{"foo": 1 "bar": 2}

[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
        T            T             F        F.           F              T  


1 -> t + 10

cur >= t + 10: true and update last print
false


"""


class Logger:

    def __init__(self): 
        self.message_to_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.message_to_timestamp or timestamp >= self.message_to_timestamp[message] + 10:
            self.message_to_timestamp[message] = timestamp
            return True

        return False
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)