"""
input: matrix (R,C)

__init__ -> O()
update -> O(1)


sumRegion -> 
    
    naive -> O( (row2 - row1) * (col2 - col1)) at most O(R*C)
    
    range sum 2D using a prefix sum matrix 
    O(R) time
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.R, self.C = len(matrix), len(matrix[0])
        
        self.horizontal_sum = []
        
        for r in range(self.R):
            row_sum = [matrix[r][0]]
            for c in range(1, self.C):
                row_sum.append(row_sum[c-1] + matrix[r][c])
            self.horizontal_sum.append(row_sum)


    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        
        for c in range(col, self.C):
            prev = 0 if c == 0 else self.horizontal_sum[row][c-1] 
            self.horizontal_sum[row][c] = prev + self.matrix[row][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        
        for r in range(row1, row2+1):
            end = self.horizontal_sum[r][col2]
            start = 0 if col1 == 0 else self.horizontal_sum[r][col1-1]
            total += end - start
        
        return total 



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)