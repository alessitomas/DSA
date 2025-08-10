"""

Solution 1: 

one pointer for each string of the arr, and the pointer move along each string.

p1 = 0
results = []

validates all strings have the same first char, move the pointer
p1 += 1
validates all strings have the same first char, move the pointer

until the pointer exceeded on string len or on string char did not match


T:  O( N * L ), where N is the arr length and L is the minimim string length
S:  O( L ) 



Solution 2:

Keep track of the longest common prefix


w1 is the cur_lcp, then iterate over the other words updating the current lcp.


Time: O(N * Lm), where N is the lenght of the arr and lm is the length of the first words.
Space: O(Lm),


"""

import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = []

        min_length = min(len(s) for s in strs)
        
        for pointer in range(min_length): 
            char = strs[0][pointer]
            
            if all(char == s[pointer] for s in strs[1:]):
                prefix.append(char)
            else:
                break 
        
        return "".join(prefix)
            

            

                

