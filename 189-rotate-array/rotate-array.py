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

time: O(N**2)
space: O(1)


[0,1,2]

[2,| 0,1]

[1,2,| 0]

mv = 3

[1,2,3,4,5]

[3,4,5 |,1,2]


Solution 3. Reverse algorithm (three reverse algorithm)





"""




class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        
        # k can be bigger than nums

        moves = k % len(nums) 

        if moves == 0:
            return 
        
        # reverse nums
        for i in range(len(nums) // 2 ):
            nums[i], nums[len(nums) - 1 - i]  = nums[len(nums) - 1 - i], nums[i]

        for i in range(moves // 2):
            nums[i], nums[ moves - 1 - i] = nums[moves - 1 - i], nums[i]


        # after moves must be reversed
        length = len(nums) - moves
        for i in range(length // 2):
            nums[moves + i], nums[ len(nums) - 1 - i] = nums[ len(nums) - 1 - i], nums[moves + i]


    