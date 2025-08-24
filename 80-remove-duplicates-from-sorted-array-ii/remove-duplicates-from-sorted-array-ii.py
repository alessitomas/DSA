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
    
        while seeker < len(nums):
        
            write_seeker = seeker + 2 >= len(nums) or nums[seeker] != nums[seeker + 2]
            if write_seeker:
                nums[writer] = nums[seeker]
                writer += 1
            seeker += 1
            
        return writer
                







        
  




        