class Solution:
    # binary search each will take 
    # time: O(log N), given that for each iteration we devide the search space N by half
    # search space is all the sorted array
    # I will use binary search to find the transition point (two values) between number smaller than target.
    # to number greater or equal to target
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        if len(nums) == 0:
            return -1
        
        if nums[l] >= target or nums[r] < target:
            if nums[l] == target:
                return l
            return -1
        
        while r - l  > 1:
            mid = (r + l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        
        return r if nums[r] == target else -1
        