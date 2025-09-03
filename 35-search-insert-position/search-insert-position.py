"""

Using binary search to find the transition point

before | after
< | >= target

loop invariants:

l pointer is always in the before area and r pointer is always in the after region, they are never the same and never cross each other
loop will exit when l and r are side by side
mid is always l > mid < r


after will be the expected index
"""



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return

        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            return 1

        l, r = 0, len(nums) - 1

        if nums[r] < target:
            return r + 1
        
        if nums[l] >= target:
            return 0

        while r > l + 1:
            mid = (r + l) // 2
            
            if nums[mid] < target:
                l = mid
            else:
                r = mid

        return r 
    


        
        