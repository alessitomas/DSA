class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        map_visited_cells = set()
        
        
        def calculate_area(position):
            stack = [position]
            map_visited_cells.add(position)
            area = 0

            while len(stack) > 0:
                i, j = stack.pop(-1)
                area += 1    
                for i_mv, j_mv in [(-1,0), (0,1), (1,0), (0, -1)]:
                    new_i = i + i_mv
                    new_j = j + j_mv
                    if (new_i >= 0 and new_i  < len(grid) 
                        and new_j  >= 0 and new_j  < len(grid[0]) 
                        and grid[new_i][new_j] != 0 
                        and (new_i, new_j) not in map_visited_cells):
                            stack.append((new_i,new_j))
                            map_visited_cells.add((new_i,new_j))
            
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell_value = grid[i][j]
                # expand
                if cell_value == 1 and (i,j) not in map_visited_cells:
                    new_area = calculate_area((i,j))
                    max_area = max(max_area, new_area)

        return max_area

                    