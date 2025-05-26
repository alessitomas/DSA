class Solution:
    # Time O ( mˆ2 nˆ2)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # for each cell, do a BFS traversal over the graph if marked the condition  
        # return True
        # add all initial positions that returned true to the answer
        from collections import deque
        def bfs_traversal(i, j, visited, pacific, atlantic, heights):      
            queue = deque([(i,j)])
            visited.add((i,j))
            
            def in_bounds(i, j):
                if (i >= 0 and i < len(heights) 
                    and j >= 0 and j < len(heights[0])):
                    return True
                return False

            while len(queue) > 0:
                i, j = queue.popleft()
                for mv_i, mv_j in [(-1,0), (0,1), (1,0), (0,-1)]:
                    new_i = i + mv_i
                    new_j = j + mv_j
                    
                    if (not in_bounds(new_i, new_j) 
                        or heights[new_i][new_j] > heights[i][j]
                        or (new_i, new_j) in visited):
                        continue

                    # update pacific if not true
                    pacific = pacific or (new_i == 0 or new_j == 0)
                    atlantic = atlantic or ((new_i == len(heights) - 1) or new_j == (len(heights[0]) - 1))

                    if pacific and atlantic:
                        return True
                    
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))
            
            return False


        pacific_atlantic = [] 
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                
                # initially connected to pacific
                pacific = i == 0 or j == 0
                # initially connected to atlantic
                atlantic = (i == len(heights) - 1) or (j == len(heights[0]) - 1)

                if (pacific and atlantic) or bfs_traversal(i, j, set(), pacific, atlantic, heights):
                    pacific_atlantic.append([i,j])

        return pacific_atlantic







        