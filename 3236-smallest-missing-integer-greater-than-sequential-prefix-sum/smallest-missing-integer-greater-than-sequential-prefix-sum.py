class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        cur_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur_sum += nums[i]
            else: 
                break
           
        while cur_sum in nums_set:
            cur_sum += 1

        return cur_sum




