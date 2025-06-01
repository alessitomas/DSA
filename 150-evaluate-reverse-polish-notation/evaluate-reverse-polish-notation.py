# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


# two solutions
# use a stack to traverse left to right and back track 2 whenever a operations is seen, calulate # it and append it to the stack
# time | space : O(N)

# ["17","+","5","+"]

# 10 * (6 / (12  * -11)) + 17 + 5

# ["5", "2", "3", "*", "+"]
# [11 ]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        def calculations(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "/":
                return int(a / b)
            elif op == "*":
                return a * b

        operations =  set(["+", "-", "/", "*"])
        # [0]
        stack = []
        # tokens = ["2", "3", "/"]
        # c = "/"
        for c in tokens:
            if c not in operations:
                stack.append(int(c))

            elif len(stack) > 1:
                # 3
                sec = stack.pop(-1) 
                # 2
                first = stack.pop(-1) 
                                
                result = calculations(first, sec, c)
                stack.append(result)
            
            else:
                return None

        if len(stack) != 1:
            return None
        
        return stack[0]