#                        0. 1. 2  3. 4  5. 6. 7
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# ans = [1,1,0,2,1,0,0,0]
# stack = [2]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        # i=5
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop(-1)
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans
            




