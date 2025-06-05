# [3,6,7,11]


# 27 / 8 -> 4
# 27 / 4 -> 8

# solution 1
# brute force
# x = for 1 ... (inf)
# subtract all piles, if it is > 0 subtract again else move on, count as a movemnt
# the first x to compelte the pile is the minimum
# O(X *  N)
# space O(N)
# piles = [3,6,7,11], h = 8

# x = 4
# [-1,-2,-1,-4]
# h = 0

# 7 / 5 -> 1.4 -> 2
# math.ceil(num / x), rounds up
# 9: 20
# solution 2
# instead of trying all possibles x in the range of [1 - MAX(N)], do a binary search instead
# to find the first x that is able to remove all bananas
# [not able | able]
# how to define if it is able or not able?
# O(N)?
# T: O(log MAX_VAL *  N)
# S: O(MAX_VAL)


# [30,11,23,4,20] , h = 5

# [1,2,3,4,5,6,7,8,9,10, ... 15 ... 30]

# l = 0
# r = 29
# mid  = 14
# (try 15) O(N)

# if not able go right
# l = mid

# else go left 
# r = mid

# until l and r are next to each other
# than it would be R (edge case L)

class Solution:
    def can_eat(self, speed : int, piles : list[int], h : int) -> bool:
        for i in range(len(piles)):
            hours_taken = math.ceil(piles[i] / speed) # round up
            h -= hours_taken
            if h < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 0:
            return 0
           
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        
        max_val = max(piles)
        
        if max_val == 0:
            return 0

        l = math.ceil(max_val/h)
        r = max_val
        
        # base case, it is the first speed
        if self.can_eat(l, piles, h):
            return l
        
        while r - l > 1:
            mid = (r + l) // 2
            # is able <-  go left
            if self.can_eat(mid, piles, h):
                r = mid
            else:
                l = mid
        
        return r


        






