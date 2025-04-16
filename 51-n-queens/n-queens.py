class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        columns_used = set()
        queens_positions = set()
        board_combinations = []
        

        def have_queen_in_diagonal(pos):
            r, c = pos
            cur_pos = (r-1,c-1)
            
            while 0 <= cur_pos[0]  and 0 <= cur_pos[1]:
                if cur_pos in queens_positions:
                    return True
                cur_pos = (cur_pos[0] -1, cur_pos[1] -1)
            
            r, c = pos
            cur_pos = (r-1,c+1)
            while 0 <= cur_pos[0] and n - 1 >= cur_pos[1]:
                if cur_pos in queens_positions:
                    return True
                cur_pos = (cur_pos[0] -1, cur_pos[1] +1)

            return False
        
        def backtracking(row, n):
            if row == n:
            # Found valid solution - create ordered column list
                col_positions = []
                for r in range(n):
                    for c in range(n):
                        if (r, c) in queens_positions:
                            col_positions.append(c)
                            break
                board_combinations.append(col_positions)
                return 

            for c in range(n):
                if (not c in columns_used 
                and not have_queen_in_diagonal((row, c))):
                
                    columns_used.add(c)
                    queens_positions.add((row,c))
                    backtracking(row+1, n)
                    columns_used.remove(c)
                    queens_positions.remove((row,c))


        backtracking(0, n)
        print(board_combinations)
        for i, bc in enumerate(board_combinations):
            new_bc = []
            for col in bc:
                default_row = ["." for i in range(n)]
                default_row[col] = "Q"
                new_bc.append("".join(default_row))
            board_combinations[i] = new_bc
            

        
        return board_combinations

        