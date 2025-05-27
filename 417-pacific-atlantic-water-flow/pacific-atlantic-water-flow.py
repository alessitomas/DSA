from collections import deque
class Solution:
    
    # cell to water
    # i, j -> ni, nj
    # height[i][j] >= height[ni][nj], in the lower ones I can use the work I've already done.

    # water to cell
    # i, j -> ni, nj
    # height[i][j] <= height[ni][nj], all nodes traversed can have their state marked.


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights is None:
            return []
        
        if len(heights) == 0:
            return []
        
        if len(heights[0]) == 0:
            return []

        def bfs(i, j, visited):
            if (i,j) in visited: return
            queue = deque([(i,j)])
            visited.add((i,j))
            
            def in_bounds(i,j):
                if i >=0 and i < len(heights) and j >= 0 and j < len(heights[0]):
                    return True
                return False
            
            while len(queue) > 0:
                cur_pos = queue.popleft()
                for mv_i, mv_j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    neigh_pos = (cur_pos[0] + mv_i, cur_pos[1] + mv_j)
                    
                    if (not in_bounds(neigh_pos[0], neigh_pos[1]) 
                        or neigh_pos in visited 
                        or heights[neigh_pos[0]][neigh_pos[1]] < heights[cur_pos[0]][cur_pos[1]]):
                        continue
                    
                    queue.append(neigh_pos)
                    visited.add(neigh_pos)



        pacific_visited = set()
        atlantic_visited = set()

        # height
        for i in range(len(heights)):
            # pacific
            bfs(i, 0, pacific_visited)
            # atlantic
            bfs(i, len(heights[0])-1, atlantic_visited)

        # width
        for i in range(len(heights[0])):
            # pacific
            bfs(0, i, pacific_visited)
            # atlantic
            bfs(len(heights)-1, i, atlantic_visited)
        
        positions = []

        for pacific_pos in pacific_visited:
            if pacific_pos in atlantic_visited:
                positions.append([pacific_pos[0], pacific_pos[1]])

        return positions










        