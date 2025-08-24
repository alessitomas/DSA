"""

nums = [1,1,1,2,2,3]

writer = 0
seeker = 0

Loop invariants:

all values on the left of writer are sorted and with most two duplicates
all values in the left of seeker were already written or should not be written

exit condition: seeker == len(nums) that will lead to all values were already written or should not be written

 
if seeker < 2 or nums[seeker] != nums[seeker - 2]:
    write 
    mv both

mv seeker



 0 1 2 3 4 5
[1,1,2,2,2,3]
 
       w
            s

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        writer = seeker = 0
        
        cur_char = nums[seeker]
        cur_count = 0
    
        while seeker < len(nums):
            
            if nums[seeker] == cur_char:
                cur_count += 1
            else:
                cur_char = nums[seeker]
                cur_count = 1


            write_seeker = seeker < 2 or 2 >= cur_count
            if write_seeker:
                nums[writer] = nums[seeker]
                writer += 1
            seeker += 1
            
        return writer
                







        
  




        