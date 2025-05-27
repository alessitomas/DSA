class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    # union find ds
    # composed only by positions "o" in the matrix 
    # map of union_find index to position in matrix
    # each index in union_find must have a flag of has edge or not
    # time O(N * N)
    # space O(N)
    
        def dfs(i,j,visited, board):
            if (i < 0 or i >= len(board) 
                or j < 0 or j >= len(board[0])
                or board[i][j] == "X"):
                return 
            
            visited.add((i,j))

            for mv_i, mv_j in [(-1,0), (0,1), (1,0), (0, -1)]:
                nw_i = i + mv_i
                nw_j = j + mv_j

                if (nw_i, nw_j) not in visited:
                    dfs(nw_i, nw_j, visited, board)
            
            return



        zeros_positions = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    zeros_positions.add((i,j))
        
        zeros_connected_to_edge = set()
        
        # height
        for i in range(len(board)):
            dfs(i, 0, zeros_connected_to_edge,board)
            dfs(i, len(board[0]) -1, zeros_connected_to_edge,board)


        # width 
        for j in range(len(board[0])):
            dfs(0, j, zeros_connected_to_edge,board)
            dfs(len(board) -1, j, zeros_connected_to_edge,board)

        for pos in zeros_positions:
            if pos not in zeros_connected_to_edge:
                board[pos[0]][pos[1]] = "X"
