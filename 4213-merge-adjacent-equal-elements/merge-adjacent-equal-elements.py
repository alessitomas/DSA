"""
navie sol

N times merge the first pair O(Nˆ2)


"""

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
                
        for n in nums:
            cur_val = n
                        
            while len(stack) > 0 and stack[-1] == cur_val:
                stack.pop()
                cur_val *= 2

            stack.append(cur_val)

        
        return stack


            

        