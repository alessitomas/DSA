"""


no need to keep the full matrix

interest data:

- current food
- current score
- snake occupied cells (tricky part since at each move without food a new position is added and the last one is removed) 

This brigs the ideia of fifo and usage of queue should be beneficial.

First in should be the first out after a move

"""

from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.R, self.C = height, width
        self.food_idx = 0
        self.food = food
        self.queue = deque([(0,0)])
        self.directions = {
            "U" : [-1, 0],
            "D" : [1, 0],
            "L" : [0, -1],
            "R": [0, 1]   
        }
        
    def in_bounds(self, r, c):    
        return 0 <= r < self.R and 0 <= c < self.C
    
    def collision(self, r, c):
        for snake_row, snake_col in self.queue:
            if r == snake_row and c == snake_col:
                return True
        return False
    
    def food_position(self, nr, nc):
        return (self.food_idx < len(self.food) and 
            self.food[self.food_idx][0] == nr and
            self.food[self.food_idx][1] == nc)
    
    def move(self, direction: str) -> int:
        if direction not in self.directions:
            return len(self.queue) - 1
        
        dr, dc = self.directions[direction]
        cur_r, cur_c = self.queue[-1]
        nr, nc = cur_r + dr, cur_c + dc
        
        if not self.in_bounds(nr, nc):
            return - 1 # game over
            
        # remove tail
        if not self.food_position(nr, nc):
            self.queue.popleft()
        else:
            self.food_idx += 1
            
        if self.collision(nr, nc):
            return -1 
        
        self.queue.append((nr, nc))
    
        return len(self.queue) - 1
        


