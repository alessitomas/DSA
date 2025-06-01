# well formed
# for every ) there must one ( before.


# first solution
# generate all possibles combinations
# verify which one are valid



# time: O(2ˆN), upper bound that would be considering invalida cases, my solution does prunning on those.
# space: O(2ˆN), upper bound
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
           
        solutions = []
        start = ["("]
        
        def backtracking(cur_state, length_left, cur_open):
            if length_left == 0:
                copy = [p for p in cur_state]
                solutions.append("".join(copy))
            
            else:
                if cur_open == 0 or length_left - cur_open >= 2:
                    cur_state.append("(")
                    backtracking(cur_state, length_left-1, cur_open+1)
                    cur_state.pop(-1)
                    
                if cur_open > 0:
                    cur_state.append(")")
                    backtracking(cur_state, length_left-1, cur_open-1)
                    cur_state.pop(-1)
            return    

                
        backtracking(start, 2*n - 1, 1)
        return solutions 