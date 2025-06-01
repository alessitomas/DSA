# try every x that could be distribuited to first
# after there is n - x candies left
# if n - x > limit * 2 -> no valid

# second at least max(0, n - x - limit), to ensure 3 does not receive more than the limit
# at most min(limit, n - x)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            ans += min(limit, n - i) - max(0, n - i - limit)  + 1
        return ans
        