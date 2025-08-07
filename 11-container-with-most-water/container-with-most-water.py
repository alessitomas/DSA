"""

area = x * y


x = j - i, we can max it out start with the most possible distance

y = min(h[i], h[j]), try to max out the min 


inwards moving the one with the least high, because there is no other match better from him.

since the distance is the max, and given it is the lowest one the height is already the max aswell.





"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while j > i:
            max_area = max(max_area, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1


        return max_area

        