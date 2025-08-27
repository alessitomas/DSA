# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

n = height + 1 
m = 2^ (height+1)  - 1


root = grid[0][ (m -1) / 2]



sub = res[r][c]

left res[r+1][c -2^ (height-r-1)]
right res[r+1][c + 2^ (height-r-1)]


                            1 (r = 0, c = 1)              h = 0    
                       2  (r = 1, c = ?)                 h = 1



m = 2^ (height+1)  - 1
2 ^ (1+ 1) -1
3

c of 2

1 - 1


["", "", ""]
["", "", ""]



Input: root = [1,2]

Output: 
[["","1",""],
 ["2","",""]]
 
 
 
Solution 1:


calculat the height of the three

create the grid before

passing down row and column thorugh arguments

pre order MID, LEFT, RIGHT 

for each node added it to the grid
 
T: O(N)
S: O(H * 2^H+1)


18 min


31 min code it up
"""


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def calculate_height(root):
            if root is None:
                return -1
            
            return max(calculate_height(root.left), calculate_height(root.right)) + 1
        
        # n = height + 1 
        # m = 2^ (height+1)  - 1
        
        def create_grid(height):
            n, m = (height + 1), 2**(height+1)  - 1
            return [[""] * m for i in range(n)]
            
        
        if root is None:
            return [[]]
        
        height = calculate_height(root)
        grid = create_grid(height)
        
        def fill_grid(r, c, node):
            nonlocal height
            if node is None:
                return
            
            grid[r][c] = str(node.val)
            
            offset = 2 ** (height - r - 1)
            fill_grid(r+1, c - offset, node.left)
            fill_grid(r+1, c + offset, node.right)
        
            
        
        fill_grid(0, ((2**(height+1)  - 1) - 1) // 2, root)
        return grid
        
        
        
        
        
       
       # 1 checked 2 // 2 = 1 
       # 
        
        
        
        
        