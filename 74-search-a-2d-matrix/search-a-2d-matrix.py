class Solution:
    # solution 1: 
    # Nested for loops, time complexity O(m*n)


    # solution 2:
    # treat matrix as flat
    
    # [0, 1 ,2]
    # [3, 4, 5]
    # m = 2
    # n = 3

    # binary search looking for target O(m*n) 
    # binary search is a valid option since there is a sorted order
    # just need to convet indices to matrix representation
    
    
    # [0, 1 ,2]
    # [3, 4, 5]

    # total n will be m * n 
    # I will treat the matrix as an array and only make conversions when trying to access te values aka (comparing, or returning)
    #  search (3):
    # use binary search to find the transition point of "before" values (< target) and "after" values (>= values).
    # if target is included, it will be the first value in the after group except edge case of being the first
    # if it is not included than matrix[r] != target
    # [0, 1 ,2|,3, 4, 5]
    
# edge cases
# [0, 1 ,2, 3, 4|5]
    def idx_matrix_map(self, idx, m, n):
        # width boundery
        row = idx // n
        col = idx % n
        return row, col



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
       
        m, n = len(matrix), len(matrix[0]) 
        l, r = 0, m * n - 1
        
        # edge case
        if matrix[0][0] == target:
            return True
        
        while r - l > 1:
            mid = (l + r) // 2
            i, j = self.idx_matrix_map(mid, m, n)
            # is before
            if matrix[i][j] < target:
                l = mid
            else:
                r = mid
        
        i, j = self.idx_matrix_map(r, m, n)
        
        return matrix[i][j] == target


             
        
        