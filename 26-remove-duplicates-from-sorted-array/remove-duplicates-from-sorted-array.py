class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = seeker = 0

        while seeker < len(nums):
            # if unique
            seeker_is_unique = seeker + 1 >= len(nums) or nums[seeker] != nums[seeker + 1]

            if seeker_is_unique:
                nums[writer] = nums[seeker]
                writer += 1
        
            seeker += 1
        
        return writer 


        