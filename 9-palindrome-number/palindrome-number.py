class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        s = str(x)
        
        lp = 0
        rp = len(s) - 1

        while rp > lp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        return True



        