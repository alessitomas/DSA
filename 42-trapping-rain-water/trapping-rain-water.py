"""
[0,1,0,2,1,0,1,3,2,1,2,1]


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest = [0] * len(height)
        right_highest = [0] * len(height)

        for i in range(1, len(height)):
            lf_max = max(left_highest[i-1], height[i-1])
            left_highest[i] = lf_max
        
        for i in reversed(range(0, len(height) - 1)):
            rt_max = max(right_highest[i+1], height[i+1])
            right_highest[i] = rt_max
        
        print(left_highest)
        print(right_highest)
        count = 0
        
        for i in range(len(height)):
            count += max(0, min(left_highest[i], right_highest[i]) - height[i])

        return count        

