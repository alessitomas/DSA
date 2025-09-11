
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






class HitCounter:
    class Node:
        def __init__(self, timestamp, nxt=None, prev=None):
            self.count = 1
            self.time = timestamp
            self.nxt = nxt
            self.prev = prev

    def __init__(self):
        self.dummy = self.Node(None)
        self.tail = self.dummy
        self.total = 0

    def clean_up(self, target_timestamp):
        # cleanup
        head = self.dummy.nxt

        while head and head.time <= (target_timestamp - 300):
            self.total -= head.count
            head.prev.nxt = head.nxt
            if head.nxt:
                head.nxt.prev = head.prev
            head = head.nxt

        if not head:
            self.tail = self.dummy    
    

    
    # O(1), max cleanup operations each time is 299
    def hit(self, timestamp: int) -> None:
        if not timestamp:
            return

        if timestamp == self.tail.time:
            self.tail.count += 1
        else:
            node = self.Node(timestamp)
            self.tail.nxt, node.prev = node, self.tail # append
            self.tail = self.tail.nxt # new tail
        
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