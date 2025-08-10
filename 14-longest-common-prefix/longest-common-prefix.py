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


Time: O(N * fL), where N is the lenght of the arr and fL is the length of the first word.
Space: O(fL)


"""

"""

Time: O(mL * N)
Space: O(Max(N, mL))

"""




"""

O(N)


--- O(L)

Time: O(N*L + L^2)


---- L, L-1, L-2, L-3, L-4, ... 1 
---- P.A: (L + 1) * L / 2

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def update_lcp(cur_lcp, cur_s):
            min_length = min(len(cur_lcp), len(cur_s))
            
            for i in range(min_length):
                if cur_lcp[i] != cur_s[i]:
                    return cur_lcp[:i]
            
            return cur_lcp[: min_length ]



        if len(strs) == 0:
            return ""
        
        lcp = list(strs[0])

        for i in range(1, len(strs)):
            
            s = strs[i]
            lcp = update_lcp(lcp, s)


        return "".join(lcp) 

        


            

            

                

