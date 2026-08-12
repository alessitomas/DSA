"""

upper bound O(nˆ2), due to naive sol

naive sol: nested loop going over all possible subarrays


lower bound O(n), due to task of view every single value at leats once


subarray pattern -> sliding window

explore with the window, if in a valid state
contract the window if in a invalid state

if in a valid state recorde the length 

keep a map of value to freq, so that we can validate if we are in a valid state or not


Time: O(N)
Space: O(N)

"""

from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k <= 0:
            return 0

        value_to_freq = defaultdict(int)
        start = 0
        max_len = 1

        for end in range(0, len(nums)):
            value_to_freq[nums[end]] += 1
            
            while value_to_freq[nums[end]] > k:
                value_to_freq[nums[start]] -= 1
                start += 1
            
            cur_length = end - start + 1
            max_len = max(cur_length, max_len)
        
        return max_len 





        