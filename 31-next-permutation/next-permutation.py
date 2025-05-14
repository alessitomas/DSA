class Solution:
    def reversedList(self, nums):
        half_index = (len(nums) // 2)
        for i in range(half_index):
            nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
            
        return nums
            
    
    def sort_before(self, nums, index):
        for i in range(index + 1, len(nums)):
            lowest = nums[i]
            lowest_index = i
            for j in range(i, len(nums)):
                if nums[j] < lowest: 
                    lowest = nums[j]
                    lowest_index = j
                    
            nums[i], nums[lowest_index] = lowest, nums[i]
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return None
            # least significantly 
            # i = [len(nums) -1,   1]
        
        for i in reversed(range(0, len(nums))):
            lowest_bigger = None
            # j= [ i-1, 0]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if lowest_bigger is None or lowest_bigger > nums[j]:
                        lowest_bigger = nums[j]
                        lowest_index = j
            if lowest_bigger is not None:
                nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
                self.sort_before(nums, i)
                return nums
                        
        
        return self.reversedList(nums)
			