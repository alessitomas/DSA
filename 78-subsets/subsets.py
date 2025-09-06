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

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtracking(idx, subset):
            subsets.append(subset.copy())
        
            for i in range(idx + 1, len(nums)):
                subset.append(nums[i]) 
                backtracking(i, subset)
                subset.pop(-1)
 
        backtracking(-1, [])
        return subsets