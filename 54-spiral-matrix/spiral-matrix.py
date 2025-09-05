class Solution:
    def is_valid(visited, r, c):
            return 0 <= r < len(visited) and 0 <= c < len(visited[0]) and visited[r][c] == 0

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        cur_dir = 0
        r, c = 0, 0
        order = []

        while len(matrix) * len(matrix[0]) > len(order):
            if Solution.is_valid(visited, r, c):
                order.append(matrix[r][c])
                visited[r][c] = 1
            else:
                r -= directions[cur_dir][0]
                c -= directions[cur_dir][1]
                cur_dir = (cur_dir + 1) % len(directions)
            
            dr, dc = directions[cur_dir]
            r += dr
            c += dc
        
        return order