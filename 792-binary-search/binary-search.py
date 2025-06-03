# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # is nice to handle base case explicity even when my code already does that?
#         i = 0
#         j = len(nums) - 1

#         while i <= j:
#             mid = ((j - i) // 2) + i
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 j = mid - 1
#             else:
#                 i = mid + 1
        
#         return - 1
        


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) 
        
        while lp < rp:
            mid = (lp + rp)  // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rp = mid 
            else:
                lp = mid + 1
        return -1


        