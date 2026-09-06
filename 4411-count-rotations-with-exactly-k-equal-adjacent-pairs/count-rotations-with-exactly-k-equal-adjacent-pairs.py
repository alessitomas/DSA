"""

"aab" s length 3

"aab" prefix legnth -> 0

score -> 1

"aba" prefix length -> 1

score -> 2

"baa" prefix length -> 1

score -> 1

2 <= n == s.length <= 100

t: <= O(nˆ3) would probably work

what is the naive solutiong?

1. Do every single possible rotation
2. calculate the score


1. Do every single possible rotation

    N - 1 possible rotations, we can leverage a deque for O(1) removal from beginning and O(1) addition to the end
    total work: O(N)

2. calculate the score

    traverse the final array O(N)


time: O(nˆ2)
space: O(n)


how to improve it?


repetitive work: 

    traverse the final array O(N)

    for every rotation the score will only change for the first char and the last one
    
    if first char == second char, score -= 1
    if the last char equals the first char score += 1

optimized sol:

time: O(N)
space: O(N)

variable for the current score
deque for constant rotations

for (N-1) cycle one char
update the variable
increment the count


using deque as a queue so that we have popleft in constant time

"""


from collections import deque

class Solution:
    def countRotations(self, s: str, k: int) -> int:
        score = count = 0
        
        for i in range(len(s) -1):
            if s[i] == s[i+1]:
                score += 1

        
        for start in range(len(s)):
            if score == k:
                count += 1
            
            if s[start] == s[(start+1) % len(s)]:
                score -= 1
            
            if s[start-1 % len(s)] == s[start]:
                score += 1
        
        return count 




            
    
        
        