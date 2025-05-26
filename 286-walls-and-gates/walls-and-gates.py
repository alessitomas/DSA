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
        # space (mn)
        gates_position = []
        
        # time (mn)
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates_position.append((i,j))


        def bfs_traversal(gate_position):
            def in_bounds(i, j):
                if (i < len(rooms) and i >= 0 
                    and j < len(rooms[0]) and j >= 0):
                    return True
                return False

            visited = set()
            visited.add(gate_position)
            # i, j, gate_dist 
            queue = deque()
            queue.append((gate_position[0], gate_position[1], 0))

            while len(queue) > 0:
                cur_cell = queue.popleft()
                i, j, dist = cur_cell
                rooms[i][j] = dist
                # up, right, down, left 
                for mv_i, mv_j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_i = i + mv_i 
                    new_j = j + mv_j
                    if (not in_bounds(new_i, new_j) 
                        or (new_i, new_j) in visited
                        or rooms[new_i][new_j] < dist + 1 
                        or rooms[new_i][new_j] == -1):
                        continue
                    
                    queue.append((new_i, new_j, dist+1))
                    visited.add((new_i, new_j))

        # time O (V * G) 
        for gate_position in gates_position:
            bfs_traversal(gate_position)
        
        return rooms