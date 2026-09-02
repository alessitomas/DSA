from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        src_r, src_c = 0 , 0
        
        R, C = len(classroom), len(classroom[0]) 

        def invalid_pos(r, c):
            return (r < 0 or r >= R) or (c < 0 or c >= C) or classroom[r][c] == "X"
        
        def is_visited(visited, next_r, next_c, cur_litter_set, cur_energy):
            if (next_r, next_c) in visited and cur_litter_set in visited[(next_r, next_c)] and visited[(next_r, next_c)][cur_litter_set] >= cur_energy:
                return True
            return False

        # 1, 2, 4, 8 
        litter_pos_to_id = {}
        
        for r in range(R):
            for c in range(C):
                if classroom[r][c] == "S":
                    src_r, src_c = r, c
                if classroom[r][c] == "L":
                    litter_pos_to_id[(r,c)] = 1 << len(litter_pos_to_id)

        litter_set = 0
        queue = deque()
        queue.append([(src_r, src_c), energy, 0, litter_set])
        visited = {(src_r, src_c): {0 : energy}}

        while queue:
            (cur_r, cur_c), cur_energy, steps, cur_litter_set = queue.popleft()

            if classroom[cur_r][cur_c] == "R":
                cur_energy = energy
            elif classroom[cur_r][cur_c] == "L":
                litter_id = litter_pos_to_id[(cur_r, cur_c)]
                cur_litter_set = cur_litter_set | litter_id

            if cur_litter_set == (1 << len(litter_pos_to_id)) - 1:
                return steps

            for dr, dc in [[0,-1],[-1,0],[0,1],[1,0]]:
                next_r = cur_r + dr
                next_c = cur_c + dc
                next_energy = cur_energy - 1
                next_steps = steps + 1

                if invalid_pos(next_r, next_c) or is_visited(visited, next_r, next_c, cur_litter_set, next_energy) or next_energy == -1:
                    continue
                
                queue.append([(next_r, next_c), next_energy, next_steps, cur_litter_set])
                visited.setdefault((next_r, next_c), dict())[cur_litter_set] = next_energy
            

        return -1
             


        
        



        
        