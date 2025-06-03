class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # is nice to handle base case explicity even when my code already does that?
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = ((j - i) // 2) + i
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        return - 1
        



        