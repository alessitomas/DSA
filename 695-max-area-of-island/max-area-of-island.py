class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        map_visited_cells = set()
        
        def calculate_area(postion, visited):
            i, j = postion
            # out of the map
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            # water or visited case
            if grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            area = 1
            visited.add((i, j))
            map_visited_cells.add((i, j))

            for i_mv, j_mv in [(-1,0), (0,1), (1,0), (0, -1)]:
                new_i = i + i_mv
                new_j = j + j_mv
                area += calculate_area((new_i, new_j), visited)
            
            return area




        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell_value = grid[i][j]
                # expand
                if cell_value == 1 and (i,j) not in map_visited_cells:
                    new_area = calculate_area((i,j), set())
                    max_area = max(max_area, new_area)

        return max_area

                    