"""

naive solution brute force 

need to max (i - i-1), where i is where skill[i] was assigned

skill -> n
station -> m

prefix 
O(m)

calculate based on n

O(M + N)


"""


class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        
        earliest = []
        s = cur_worker = 0
        # earlist
        while cur_worker < len(skill) and s < len(station):
            if station[s] == skill[cur_worker]:
                earliest.append(s)
                cur_worker += 1
            s += 1

        latest = [0] * len(skill)
        s = len(station) - 1
        cur_worker = len(skill) -1
        
        # latest 
        while cur_worker >= 0 and s >= 0:
            if station[s] == skill[cur_worker]:
                latest[cur_worker] = s
                cur_worker -= 1
            s -= 1

        gap = 0
        
        for i in range(1, len(skill)):
            cur_gap = latest[i] - earliest[i-1]
            gap = max(gap, cur_gap)

        

        return gap



        