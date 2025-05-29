#
#.   s1 - s2
#.   |
#.   s3 -------- s4  --- s7
#                 |
#          s5---- s6




#
#.   s1 --------- s2
#.    
#.    |      s3.   |
#                
#     s4 -------  s5 _ --- s6


# {c:{0:0, 2: 1}, r:{0:0}}

# (0,0) - (0, 2)
# [0,0] - [0,1] _ [1,0],[1,2],[2,1],[2,2]
# (0,0) - (0,2)
#               0.    1.   2.    3.    4    
#. stones = [[0,0], [0,1],[1,0],[1,2],[2,1],[2,2]]
# parent [0, 1, 2, 3 ,4]
# size  [1,1,1,1,1]

# time O(N * a(N))
# space O(N)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if stones is None:
            return None

        if len(stones) < 2:
            return 0

        stones_represent = {"c": {}, "r":{}}

        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
            
            def find(self, index):
                # find root
                root = index
                while root != self.parent[root]:
                    root = self.parent[root]
                # path compression
                while index != root:
                    cur_parent = self.parent[index]
                    self.parent[index] = root
                    index = cur_parent

                return root 
                
            def union(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                if root_a == root_b:
                    return
                
                if self.rank[root_a] > self.rank[root_b]:
                    self.parent[root_b] = root_a
                else:
                    if self.rank[root_a] == self.rank[root_b]:
                        self.rank[root_b] += 1
                    self.parent[root_a] = root_b




        uf = DSU(len(stones))

        for stone_index, (r, c) in enumerate(stones):
            # row
            if r not in stones_represent["r"]:
                stones_represent["r"][r] = stone_index
            else:
                uf.union(stone_index, stones_represent["r"][r])
            # col 
            if c not in stones_represent["c"]:
                stones_represent["c"][c] = stone_index
            else:
                uf.union(stone_index, stones_represent["c"][c])

        count_removed = 0
        root_visited = set()
        for i in range(len(stones)):
            root = uf.find(i)
            if root not in root_visited:
                root_visited.add(root)
            else:
                count_removed += 1
        return count_removed






        