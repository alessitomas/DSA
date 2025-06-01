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


    

    def distributeCandies(self, n: int, limit: int) -> int:
        solutions = 0
        def backtracking(state, candies_left, limit, par_idx):
            nonlocal solutions
            if candies_left == 0:
                solutions += 1
                state[par_idx] -= 1
                return 
            
            possible_give_amount = limit * (3 - par_idx)
            
            for i in range(3):
                if i >= par_idx:
                    possible_give_amount -= state[i]

            if candies_left > possible_give_amount:
                state[par_idx] -= 1
                return 

            # backtracK ? 
            # give to one
            if state[0] <  limit and par_idx <= 0:
                state[0] += 1 
                backtracking(state, candies_left-1, limit, 0)
            
            # give to 2
            if state[1] <  limit and par_idx <= 1:
                state[1] += 1 
                backtracking(state, candies_left-1, limit, 1)
            
            # give to 3
            if state[2] <  limit and par_idx <= 2:
                state[2] += 1 
                backtracking(state, candies_left-1, limit, 2)
            
            state[par_idx] -= 1
        
        backtracking([0,0,0], n, limit, 0)
        return solutions
        
        