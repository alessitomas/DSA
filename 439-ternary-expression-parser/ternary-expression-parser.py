"""
Triggers:

MAJOR: "NESTED"
MINOR: EXPRESSION 


T/F ? (RETURN IF TRUE) : (RETURN IF FALSE)

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'


1. return will be one digit or one char
2. when we have a evaluation there is a section that we can discard, either before ":" or after ":"
3. I can use indices (start, end) to keep track of the valid range
4. If True, start += 2 and end will move to left until after ":" 
5. If False, start will move right until after ":"  end stays the same

chained up operations

1. recursion nature
2. opt to use recursion or a iterative based algorithm with stack

3. while loop with two-pointers (optimal and easier) 
 - ERROR: Last detect ":" could not be the else excpetion for th condition you're evaludating 
  s
T?3:T?2:7
      e

T?F?3:2:T?2:7

"""


class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        open_to_close = {}

        for i, c in enumerate(expression):
            if c == "?":
                stack.append(i)
            elif c == ":":
                open_to_close[stack.pop()] = i
            

        start = 0
        end = len(expression) -1

        while end > start:
            if expression[start] == "T":
                end = open_to_close[start+1] - 1
                start += 2
            else:
                start = open_to_close[start+1] + 1

        return expression[start]




        

        


        

