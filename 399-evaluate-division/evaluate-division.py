"""

Solution 1 BFS:

T: O(E + Q * (E))
S: O(E)


Solution 2 Union-Find:

Union-Find aggregate connected components and is possible to store the relation between son and parent, using weights.

T: O(E + Q * a(E)) ->O(E + Q)
S: O(E)

"""


from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class DSU:
            def __init__(self):
                self.parent = dict()
                self.weight = dict()
                self.rank = dict()

            def init_sets(self, node):
                if node not in self.parent:
                    self.parent[node] = node
                    self.weight[node] = 1.0
                    self.rank[node] = 0
            
            def find(self, node):
                # find root
                if node not in self.parent:
                    return 

                root = node
                cum_ratio_to_root = 1.0
                
                while self.parent[root] != root:
                    cum_ratio_to_root *= self.weight[root]
                    root = self.parent[root]

                # path compression
                while node != root:
                    next_parent = self.parent[node]
                    self.parent[node] = root
                    cur_weight = self.weight[node]
                    self.weight[node] = cum_ratio_to_root
                    cum_ratio_to_root /= cur_weight
                    node = next_parent
                
                return root

            def union(self, src, dst, val):
            # (a/b) = val
            # (a/root_a) = w[a]
            # (root_a) = a / w[a]
            # (b/root_b) = w[b]
            # (root_b) = b / w[b]

            # (a / w[a]) / (b / w[b]) -> (a * w[b] / w[a] * b). 
            # (a/b) * w[b] / w[a]

            # (root_a / root_b) = (a/b) * w[b] / w[a]
            # (root_a / root_b) = val * w[b] / w[a]


            # weight[root_x] = (x/y) * (y/root_y) / (x/root_x)
        
                root_src, root_dst = self.find(src), self.find(dst)
                
                if not root_src or not root_dst:
                    return

                rank_src, rank_dst = self.rank[root_src], self.rank[root_dst]
                
                if rank_src > rank_dst:
                    self.parent[root_dst] = root_src
                    self.weight[root_dst] = 1 / (val * self.weight[dst] / self.weight[src])
                elif rank_src < rank_dst:
                    # (root_a / root_b) = val * w[b] / w[a]
                    self.parent[root_src] = root_dst
                    self.weight[root_src] = val * self.weight[dst] / self.weight[src]
                else: 
                    self.parent[root_dst] = root_src
                    self.weight[root_dst] = 1 / (val * self.weight[dst] / self.weight[src])
                    self.rank[root_src] += 1
            
            def calculate_eq(self, src, dst):
                root_src, root_dst = self.find(src), self.find(dst)
                
                if not root_src or not root_dst or root_src != root_dst:
                    return -1.0 
                
                return self.weight[src] / self.weight[dst]

        dsu = DSU()
        for (src, dst), val in zip(equations, values):
            dsu.init_sets(src)
            dsu.init_sets(dst)

            dsu.union(src, dst, val)

        results = list()
        
        for q_src, q_dst in queries:
            results.append(dsu.calculate_eq(q_src, q_dst))

        return results 
            


        

     
            
            
            
            
            
        