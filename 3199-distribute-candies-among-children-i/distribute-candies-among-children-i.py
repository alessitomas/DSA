class Solution:
    # n candies
    # limit per child
    # 3 children
    

    # Arranjo.  
    # All combinations where the order matters, but needs to sum to n, and limit per child
    # 
    # 
    # Solution, backtracking to create all possibilities
    # branches give to child 1 or give to child 2 or give to child 3
    #
    # time complexity: 3ˆN
    # space complexity: N


    # prunning to avoid getting the same final state more than once
    # once you give to child i you can give it more to child i-1


    # [0,0,0]
    # they will be forever differently
    # i = 0 -> [1,0,0]
    # i = 2 -> [0,1,0]
    # i = 3 -> [0,0,1]


# [0,0,0]               # [0, 1, 0]
# [1,0,0]              # [0, 2, 0]
# [2,0,0]
# [3,0,0]

            
    def three_sum(self, target, possible_nums):
        unique_combinations = 0
        for i in range(len(possible_nums) - 2):
            # no duplicates
            if i > 0 and possible_nums[i] == possible_nums[i-1]:
                continue
            j = i + 1
            k = len(possible_nums) - 1
            matching = target - possible_nums[i]
            while k > j:
                cur_sum = possible_nums[j] + possible_nums[k]
                if cur_sum < matching:
                    j += 1
                    # no duplicates
                elif cur_sum > matching:
                    k -= 1
                else:
                    if (possible_nums[i] == possible_nums[j] 
                        and possible_nums[j] == possible_nums[k]):
                        unique_combinations += 1
                    elif (possible_nums[i] != possible_nums[j] 
                        and possible_nums[j] != possible_nums[k]):
                        unique_combinations += 6
                    else:
                        unique_combinations += 3
                    
                    prev_j = possible_nums[j]
                    j += 1
                    while j < k and prev_j == possible_nums[j]:
                        j += 1
                    k -= 1

        return unique_combinations
    
    def distributeCandies(self, n: int, limit: int) -> int:
        possible_nums = []
        
        for i in range(limit+1):
            for _ in range(3):
                possible_nums.append(i)

        combinations = self.three_sum(n, possible_nums)
        # each combination can permute
        # permutation of 3 chars: 3, 2, 1 -> 6
        return combinations 
