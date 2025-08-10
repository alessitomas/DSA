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


Solution 3. Reverse algorithm (three reverse algorithm)

T: O(N)
S: O(1)



nums = [1,2,3,4,5,6,7], k = 4

nums = [7,1,2,3,4,5,6]
nums = [6,7,1,2,3,4,5]
nums = [5,6,7,1,2,3,4]


nums = [4,5,6,7,1,2,3]

--------------------------------------------------------
k = 4
nums = [1,2,3,4,5,6,7]

nums = [4,5,6,7,| 1,2,3]


nums = [1,2,3,4,5,6,7]

nums = [7,6,5,4,| 3,2,1]

nums = [4,5,6,7,| 1,2,3]






"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0  # number of elements moved
        
        for start in range(n):
            if count >= n:
                break
            
            current = start
            prev_value = nums[start]
            
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev_value = prev_value, nums[next_idx]
                current = next_idx
                count += 1
                
                if current == start:
                    break
