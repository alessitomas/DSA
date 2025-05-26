from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Matrix can be seen as a graph problem
        # 1. Store the position of each gate
        # 2. For each gate do a BFS traversal over the matrix, update the cell value if the # distance to the gate is less then the value of the cell

        # 1. Store the position of each gate
        
        # time (mn)
        gates_position = []
        INF = 2**31 - 1 
        
        # time (mn)
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates_position.append((i,j))

        # time (mn)
        def bfs_traversal(gates_position):
            def in_bounds(i, j):
                if (i < len(rooms) and i >= 0 
                    and j < len(rooms[0]) and j >= 0):
                    return True
                return False

            # i, j, gate_dist 
            # SPACE (mn)
            queue = deque(gates_position)            

            while len(queue) > 0:
                cur_cell = queue.popleft()
                i, j = cur_cell
                
                # up, right, down, left 
                for mv_i, mv_j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_i = i + mv_i 
                    new_j = j + mv_j
                    if (not in_bounds(new_i, new_j) 
                        or rooms[new_i][new_j] != INF):
                        continue
                    
                    queue.append((new_i, new_j))
                    rooms[new_i][new_j] = rooms[i][j] + 1
                

   
        bfs_traversal(gates_position)
        
        return rooms