class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = seeker = 0

        while seeker < len(nums):
            # if unique
            seeker_is_unique = seeker == 0 or nums[seeker] != nums[seeker - 1]

            if seeker_is_unique:
                nums[writer] = nums[seeker]
                writer += 1
                seeker += 1
            else:
                seeker += 1
        
        return writer 


        