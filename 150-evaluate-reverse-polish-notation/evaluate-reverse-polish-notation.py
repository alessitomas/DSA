# Time and Space: O(N), all one time. Every time I see a (operand) o do 2 cosntant time op
# max possible number of operands is < N
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return int(tokens[0])
        
        def dfs():
            cur_char = tokens.pop()
            if cur_char not in "+-/*":
                return int(cur_char)
            
            second = dfs()
            first = dfs()

            match cur_char:
                case "+":
                    return first + second
                case "-":
                    return first - second
                case "/":
                    return int(first / second)
                case "*":
                    return first * second


        return dfs()