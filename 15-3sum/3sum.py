
"""

Solution 2:

T: O(Nˆ2)
S: O(N)

 0 1 2
[1,2,3]

len = 3


"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1
            while end > start:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                if end < len(nums) - 1 and nums[end] == nums[end + 1]:
                    end -= 1
                    continue

                cur_sum = nums[start] + nums[end] + nums[i]
                if cur_sum > 0:
                    end -= 1
                elif cur_sum < 0:
                    start += 1
                else:
                    triplets.add((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1


        return [ [t[0], t[1], t[2] ] for t in triplets]





                
                
                

                    
                
        
        