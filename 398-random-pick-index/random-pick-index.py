from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.key_to_idx = defaultdict(list)
        for i, v in enumerate(nums):
            self.key_to_idx[v].append(i)
        

    def pick(self, target: int) -> int:
        if target not in self.key_to_idx:
            return -1
        return random.choice(self.key_to_idx[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)