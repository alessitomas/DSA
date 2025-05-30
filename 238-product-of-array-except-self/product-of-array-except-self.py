# brute force would be
# 2 nested for loops
# multiply and add to answer array

# O(Nˆ2) nested loops
# append in dynamic array amortized O(1)


# performant soluiton
# prefix and sufix multiplication


# prefix [1,2,6,24]

# sufix [24,24,12,4]

[24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        if len(nums) < 2:
            return nums

        prefix_mul = []
        cum_mul = 1
        
        for i in range(0, len(nums)):
            cum_mul *= nums[i]
            prefix_mul.append(cum_mul)


        suffix_mul = []
        cum_mul = 1
                
        for i in reversed(range(0, len(nums))):
            cum_mul *= nums[i]
            suffix_mul.append(cum_mul)
        
        suffix_mul = suffix_mul[::-1]

        ans = []

        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            if i > 0:
                prefix = prefix_mul[i-1]
            if i < len(nums) -1:
                suffix  = suffix_mul[i+1]
                
            ans.append(prefix * suffix)
        return ans