"""

BFS, because visited by distance 


Multi-source BFS with all gates postions

Visit all reachable empty positions, keep track of the visited position to avoid infinite loop or revisiting with a major distance.

Avoid visiting gates, avoid visiting walls and avoid visiting already visited cells.

I can use the rooms matrix to keep track of the visited cells.

optimal:

t: O( R*C )
s: O( R*C ), due to the queue for every cell with can append a constant number of neighboors

"""


from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # edge case
        if not rooms or not rooms[0]:
            return 
        
        R, C = len(rooms), len(rooms[0])
        # queue init with gates
        queue = deque()
        
        for i in range(R):
            for j in range(C):
                
                if rooms[i][j] == 0:
                    queue.append( 
                        (i, j, 0)
                    )
        
        def in_bounds(row, column):
            return 0 <= row < R and 0 <= column < C 
            
        def bfs_traversal():
            EMPTY = 2**31 -1
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            
            while len(queue) > 0:
                row, col, dist = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if not in_bounds(nr, nc) or rooms[nr][nc] != EMPTY:
                        continue
                    
                    queue.append(
                        (nr, nc, dist + 1)
                    )   
                    rooms[nr][nc] = dist + 1

        bfs_traversal()
        

        
        