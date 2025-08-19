"""

Solution 1: 


Create a graph from the jump array where: 


i -> j, if i can jump to j index.


Than using dfs verify of index 0 can reach index len(nums) -1

T: O( V + E ), in this case V is N and E in the worst case is N ** 2 so it can be descbribed as O(N**2)
S: O( V + E ) 


Solution 2:

Greddy algorithm, keep track of the best so far.

Local optimal will lead to global optimal

"""

from collections import defaultdict
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False 

        max_reachable = 0

        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            else:
                max_reachable = max(max_reachable, i + nums[i])

            
        return True





        