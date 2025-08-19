"""

Solution 1: 


Create a graph from the jump array where: 


i -> j, if i can jump to j index.


Than using dfs verify of index 0 can reach index len(nums) -1

T: O( V + E )
S: O( V + E ) 


"""

from collections import defaultdict
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False 

        visited = set()

        def dfs(cur_index, target):
            
            if cur_index in visited:
                return False
            
            if cur_index >= target:
                return True

            visited.add(cur_index)

            for jmp in range(1, nums[cur_index] + 1):
                if dfs(cur_index + jmp, target):
                    return True

            return False


        return dfs(0, len(nums) - 1)



        