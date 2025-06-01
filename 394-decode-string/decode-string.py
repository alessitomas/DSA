# "3[a2[c]]"

# stack = [3, [, a, c, c]

# cca

# "3[a2[c]]"
# stack [c, c, a, c, c, a, c, c, a] -> "accaccacc"

# segment = "cca" ccaccacca
# "acc".          accaccacc


# Iterative with and stack
# (K * n, + K * n, + K * n), this sum reprate countK time, count K cant be mroe than N
# nested (K * (k* n) -> K ˆ2 * n
# time: O(KˆnestedK + maxEncodedSize)
# space: O(KˆnestedK + maxEncodedSize)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                segment = []
                top = stack.pop(-1)
                # done with the segment
                while len(stack) > 0 and top != "[":
                    segment.append(top)
                    top = stack.pop(-1)
                # collect num
                num = []
                while len(stack) > 0 and stack[-1].isdigit():
                    num.append(stack.pop(-1))
                # stack is LIFO, so lets reverse it
                segment = segment[::-1]
                num = num[::-1]
                for i in range(int("".join(num))):
                    for c in segment:
                        stack.append(c)
        return "".join(stack)

                

            
