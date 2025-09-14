"""
[0,1,0,2,1,0,1,3,2,1,2,1]


"""

# # T: O(N)
# # S: O(N)

"""
edge case handling:

    - empty array instantly return 0
    - array of size one, skip prefix loops, go straight to the count loop. Will return 0 since both max left and right are 0.
    - all same height will return 0 since max of left and right heighst will equal current height
"""

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0 

#         left_highest = [0] * len(height)
#         right_highest = [0] * len(height)

#         for i in range(1, len(height)):
#             lf_max = max(left_highest[i-1], height[i-1])
#             left_highest[i] = lf_max
        
#         for i in reversed(range(0, len(height) - 1)):
#             rt_max = max(right_highest[i+1], height[i+1])
#             right_highest[i] = rt_max

#         count = 0
        
#         for i in range(len(height)):
#             count += max(0, min(left_highest[i], right_highest[i]) - height[i])

        # return count        



# # T: O(N**2)
# # S: O(1)
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         def get_max(index):
#             l, r = 0, len(height) - 1
#             l_max = r_max = 0

#             while l < index:
#                 l_max = max(l_max, height[l])
#                 l += 1
            

#             while r > index:
#                 r_max = max(r_max, height[r])
#                 r -= 1

#             return l_max, r_max


#         count = 0
#         for i in range(len(height)):
#             count += max(0, min(get_max(i)) - height[i])

#         return count        

# Two-pointer solution
# T: O(N)
# S: O(1)


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left_max, right_max = height[0], height[-1]
        lp, rp = 1, len(height) - 2
        count = 0
        
        while rp >= lp:
            if left_max <= right_max:
                count += max(0, left_max - height[lp])
                left_max = max(left_max, height[lp])
                lp += 1
            else:
                count += max(0, right_max - height[rp])
                right_max = max(right_max, height[rp])
                rp -= 1
        return count 



