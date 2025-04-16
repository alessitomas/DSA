class LRUCache:
    class LLNode:
        def __init__(self, key=None, value=None, next=None, prev=None):
            self.value = value
            self.key = key
            self.next = next
            self.prev = prev
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.key_value = {}
        dummy = LRUCache.LLNode()
        self.head = dummy
        self.tail = dummy
    
    def update_mru(self, node, is_new):
        if node == self.tail:
            return
        
        if not is_new:
            n_prev = node.prev
            n_next = node.next

            n_prev.next = n_next 
            if node != self.tail:
                n_next.prev = n_prev 
            node.next = None
        if self.size == 0:
            self.head.next 
        self.tail.next = node
        node.prev = self.tail
        self.tail = node



    def get(self, key: int) -> int:
        if key in self.key_value:
            node = self.key_value[key]
            self.update_mru(node, False)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_value:
            node = self.key_value[key]
            node.value = value
            self.update_mru(node, False)
        else:
            if self.size == len(self.key_value):
                lru_node = self.head.next
                self.key_value.pop(lru_node.key)
                self.head = self.head.next
        
            node = self.LLNode(key, value)
            self.key_value[key] = node
            self.update_mru(node, True)

    
            
# d -> None



# push 0

# 0 ->

# push 1

# 0 -> 1

# push 2

# 0 -> 1 - > 2

# put 0

# 1 -> 2 -> 0

# put 5

# 1 -> 2 -> 0 -> 5

# put 6

# 2 <-> 0 <-> 5 <-> 6

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)