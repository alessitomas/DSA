"""

Is possible to represent the matrix as a graph, where each (r, c) position represents a node in the graph and each node is connected to its adjacents neighbors up, down, left or right.



One possibility is to first differenciate land of one island from land of another island, I can do that by first traversing the hole matrix and flipping island 1 values to 2.

Then I just need to start a BFS on water neighbors from every node in island 1, keeping track of the number of water island in that path, when I find the first land of island 2 than I'm certain that the length of that path is the lowest possible path for the staring land of island 1.


Doing it for every node in the island 1 I can get the lowest path of all lands.

I can't do just one BFS because I can't have path that is not the shortest to a given cell but is the one with the least number of water lands


I don't need to flip it I can just added it to a set()
"""

from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        
        R, C = len(grid), len(grid[0])
        
        island_one = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def valid_cell(r, c):
            return 0 <= r < R and 0 <= c < C

        def visit_island(r, c):
            queue = deque([(r,c)])
            island_one.add((r,c))
            
            while len(queue) > 0:
                cur_r, cur_c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc

                    if (nr, nc) in island_one or not valid_cell(nr, nc) or grid[nr][nc] != 1:
                        continue

                    queue.append((nr, nc))
                    island_one.add((nr, nc))
            
        def get_first_land():
            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 1:
                        return i, j
            return -1, -1
        
        first_r, first_c = get_first_land()
        
        visit_island(first_r, first_c)

        shortest_path = float("inf")
        
        def get_shortest_path(r, c):
            visited = set( [(r, c)] )
            # queue: (r, c, water_in_path)
            queue = deque([(r, c, 0)])

            while len(queue) > 0:
                cur_r, cur_c, cur_path = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc

                    if (nr, nc) in island_one or not valid_cell(nr, nc) or (nr, nc) in visited:
                        continue

                    if grid[nr][nc] == 1:
                        return cur_path

                    queue.append((nr, nc, cur_path + 1))
                    visited.add((nr, nc))

            return float("inf")

        
        for land_r, land_c in island_one:
            shortest_path = min(shortest_path, get_shortest_path(land_r, land_c))
                    
        return shortest_path



        # 1.1 init globla min path 

        # 2. for every cell node in island 1
            # do a BFS and calculate the smallest path for that given cell
            # update the best overall

        
        # 3 return the best overall 
    