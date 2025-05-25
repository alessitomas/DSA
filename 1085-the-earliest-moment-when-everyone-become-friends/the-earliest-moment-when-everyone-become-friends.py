class Solution:

    # Time: O(M LOG M + N + Ma(N)), where M is the number of edges and N is the number of nodes.
    # Space: O(N)
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        class DSU:
            def __init__(self, n):
                self.components = n
                self.rank = [1 for i in range(n)]
                self.parent = [i for i in range(n)]
            def find(self, node):
                root = node
                while root != self.parent[root]:
                    root = self.parent[root]
                while node != root:
                    # 2
                    old_parent = self.parent[node]
                    self.parent[node] = root
                    node = old_parent
                
                return root
            
    
            def union(self, node_a, node_b):
                root_a = self.find(node_a)
                root_b = self.find(node_b)
                
                if root_a == root_b:
                    return False
                
                if self.rank[root_a] >= self.rank[root_b]:
                    self.parent[root_b] = root_a
                    if self.rank[root_a] == self.rank[root_b]:
                        self.rank[root_a] += 1
                else:
                    self.parent[root_a] = root_b
                
                self.components -= 1
                return self.components == 1
        
        if len(logs) < n-1:
            return -1

        dsu = DSU(n)
        logs.sort(key= lambda x: x[0])
        
        for timestamp, a, b in logs:
            if dsu.union(a,b):
                return timestamp
        return -1
                    
        