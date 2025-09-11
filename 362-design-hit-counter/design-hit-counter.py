
"""
 1         301
 |-----------|

getHits( x )

(x-300, x] 


"""

"""




1 -> 2 -> 3 -> 4 -> 300 -> 300 -> 301

I could create a total count per second, array.

For every hit I would increment the count from it timestamp and also the next 299.
hit would be cosntant O(1)

Get hits would be constant just the need to acess hte index value.

bottleneck and problem 1 <= timestamp <= 2 * 10ˆ9, at most 2 billion bit space occupied.




Queue that only stores hits in the last 300 seconds?


new hit 

have a global value with the total cumulative sum

IF equals last registered add its count
Else add a new time recording with count 1
pop any starting node that has a timestamp <= X - 300


O(1), since the queue will have at most 300 nodes

get hits:


O(1), get it from global variable


["hit","getHits"]

[[301],[301]]

return 4
return 5
T = 6

c 3 -> 2 -> 1
n 1 -> 300 -> 301
"""

from collections import deque
class HitCounter:
    def __init__(self):
        # [timestamp, count], because count is mutable
        self.queue = deque()
        self.total = 0

    def clean_up(self, target_timestamp):
        while len(self.queue) > 0 and self.queue[0][0] <= (target_timestamp - 300):
            self.total -= self.queue[0][1]
            self.queue.popleft()
    
    # O(1), max cleanup operations each time is 299
    def hit(self, timestamp: int) -> None:
        
        if not timestamp:
            return

        if len(self.queue) > 0 and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append(
                [timestamp, 1]
            )
            
        self.total += 1
        self.clean_up(timestamp)

    

    # O(1)
    def getHits(self, timestamp: int) -> int:
        self.clean_up(timestamp)
        return self.total 
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)