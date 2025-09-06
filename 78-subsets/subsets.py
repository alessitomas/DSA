"""

Integer array nums of unique elements

 0 1 2.    
[1,2,3]

C n 1
C n 2
C n 3
...
                            dummy.      - 1

                       0    1    2     
                     1   2   2.            


                   [1].      [2].     [3]

If I do a backtracking where each node represents a unique subset I can add all of them into the input array and return it.


I can use the index of the array to know what integer to add to the subset and what other options I still can add.

By only adding values that have a index > than the current since the array is unique it is guaranteed that each subset will be unique.


is there a need to explicit a base case? Since index will be already bounded?

T: O( Nˆ3 ), Nˆ2 nodes N iterations per node
S: O(N), recursion stack

17 minutes to code it up

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtracking(idx, subset):
            subsets.append(subset.copy())
        
            for i in range(idx, len(nums)):
                subset.append(nums[i]) 
                backtracking(i + 1, subset)
                subset.pop(-1)
 
        backtracking(0, [])
        return subsets

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         """
#         Generate all subsets (the power set) via backtracking.
#         Time: O(n * 2^n), total node 2ˆN since there are N values and each one has the option of being included of not included.

#         Aux Space: O(n) + output
#         """
#         res: List[List[int]] = []
#         n = len(nums)

#         def dfs(start: int, path: List[int]) -> None:
#             # Record the current subset
#             res.append(path.copy())
#             # Explore further choices
#             for i in range(start, n):
#                 path.append(nums[i])
#                 dfs(i + 1, path)
#                 path.pop()  # backtrack

#         dfs(0, [])
#         return res