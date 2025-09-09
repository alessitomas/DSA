# 0, 1, 2, 3, 4, 5, 6, 7, 8
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
# 9x9 grid

# return true no conflits
# retrun false
# numbers 0-9

# zeros denote empty cells

# Totally forgot that zeros denote empty cells!!!!!!!!!! [CRAZY]


# conflict

# duplicate number (other than 0) along a row, column or 3x3 subgrid.

        """
        Solution one:

        validate rows, using a set
            for row 
                for column

        validate columns, using a set
            for column
                for row

        validate subgrids, using a set for duplicates

        I can always start at the left most and up most position of each subgrid.

        first one (0,0)
        second one (0, 3)
        third one (0, 6)

        c += 3 until 6
        r += 3 and c = 0

        fourth (3, 0)
        5 (3, 3)
        6 (3, 6)
        7 (6, 0)
        8 (6, 3)
        9 (6, 6)



        T: O(M*N) in sudoku case 9x9 O(1)
        S: O(max(m*n)) in sudoku case 9x9 O(1)


        """

        grid = board
        N = 9
        if not grid or len(grid) != N or len(grid[0]) != N:
            return False
        
        # row verification
        for i in range(N):
            duplicates = set()
            for j in range(N):
                if grid[i][j] == ".":
                    continue
                if grid[i][j] in duplicates:
                    return False
                duplicates.add(grid[i][j])

        # column verification
        for j in range(N):
            duplicates = set()
            for i in range(N):
                if grid[i][j] == ".":
                    continue
                if grid[i][j] in duplicates:
                    return False
                duplicates.add(grid[i][j])

        # subgrid verification
        def valid_subgrid(start_r, start_c):
            duplicates = set()
            for i in range(start_r, start_r + 3):
                for j in range(start_c, start_c + 3):
                    if grid[i][j] == ".":
                        continue
                    if grid[i][j] in duplicates:
                        return False
                    duplicates.add(grid[i][j])
            return True

        
        for r in range(0, 3):
            for c in range(0, 3):
                if not valid_subgrid(r * 3, c * 3 ):
                    return False
        
        # (0,0)
        # (0,3)
        # (0,6)

        # (3,0)
        # (3,3)
        # (3,6)

        # (6,0)
        # (6,3)
        # (6,6)

        return True

                
            


        