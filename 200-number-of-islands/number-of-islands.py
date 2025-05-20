from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_cell = set()

        def dfs_expand(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 
            if grid[i][j] == "0":
                return 
            if (i, j) in visited_cell:
                return 
            
            visited_cell.add((i,j))

            for i_mv, j_mv in [(-1,0),(0,1),(1,0),(0,-1)]:
                i_new = i + i_mv
                j_new = j + j_mv
                dfs_expand(i_new, j_new)
        
        def bfs_expand(i, j):
            queue = deque()
            queue.append((i,j))
            visited_cell.add((i,j))

            while len(queue) > 0:
                i, j = queue.popleft()
                for i_mv, j_mv in [(-1,0),(0,1),(1,0),(0,-1)]:
                    i_new = i + i_mv
                    j_new = j + j_mv
                    if (i_new >= 0 and i_new < len(grid)
                        and j_new >= 0 and j_new < len(grid[0])
                        and (i_new, j_new) not in visited_cell
                        and grid[i_new][j_new] == "1"):
                            bfs_expand(i_new, j_new)
                            visited_cell.add((i_new,j_new))
            return 


        
        island_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited_cell:
                    bfs_expand(i,j)
                    island_count += 1
        
        return island_count