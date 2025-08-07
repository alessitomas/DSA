"""

Solution 1:

time: O(N)
space: O(N)

Create a new arr with the same size as the original, with a default value.

Traverse the orignal array and for each index calculate the index in the new array: (i + k) % len(array)



Solution 2:

For every K shift right all values one time, and the last go to the front.

for i in range k
    shift right

time: O(K * N)
space: O(1)


"""




class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        nums_cpy = [v for v in nums]

        for i in range(len(nums)):
            new_idx = (i + k) % len(nums)
            nums[new_idx] = nums_cpy[i]


    