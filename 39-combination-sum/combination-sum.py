"""
i             0 1 2 3
candidates = [2,3,6,7]
target = 7

Given that candidates it is a distinct array, integer in different position will differ.
With that I only need to avoid making the same combination of indices.


To generate all combinations I can do a dfs backtracking.

                        0                       0

            0        1.       2.      3  
          1 2 3     2  3      3

Where each node represents the current sum, I will be passing as argument what is the current index to be added

base case when i >= len(candidates): return

when sum is meet add it and return


to avoid making the same combination of indeces for each index a could only branch on indeces bigger than it.

for i in range(i, len(candidates)):
    backtracking(i+1)


I can also prune any sum that is bigger than the 




T: O(NˆN * N)
S: O(NˆN)

"""



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        combinations = []
        
        # candidates [2,3,6,7]
        # target 8

        #.                  0        0.       []
        def backtracking(cur_idx, cur_sum, cur_comb):
            #            >= 4                          >= 8
            if cur_sum >= target:
                if cur_sum == target:
                    combinations.append(cur_comb.copy())
                return 

            for i in range(cur_idx, len(candidates)):
                
                cur_comb.append(candidates[i]) # add it to the sequence
                backtracking(i, cur_sum + candidates[i], cur_comb) # recurse on next index
                cur_comb.pop() # backtracking
            
        backtracking(0, 0, [])
        
        return combinations

"""
                                             0
                                       0   1.  2   3
                            [0,0]   [0,1]  2   3






backtracking(1, 2, [2])
backtracking(1, 2, [2])
backtracking(0, 0, [])
stack

target = 8

[2,3,6,7]


"""