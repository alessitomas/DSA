class Solution:
    # 1 indexed
    
    # DFS or BFS, keeping a global visited
    # Creation of adjancency_list 
    # Time O(N + E)
    # Space O(N + E)

    
    # Union Find, and detect cycle
    # Time O(N)
    # Space O(N)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges or not edges[0]:
            return
            
        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]

            def find(self, node):
                # find root
                root = node
                while root != self.parent[root]:
                    root = self.parent[root]
                # path compression
                while node != root:
                    old_parent = self.parent[node]
                    self.parent[node] = root
                    node = old_parent
                return root
            
            def union(self, a, b):
                # 1 indexed to 0 indexed
                root_a = self.find(a -1)
                root_b = self.find(b -1)

                if root_a == root_b:
                    return True
                
                if self.rank[root_a] > self.rank[root_b]:
                    self.parent[root_b] = root_a
                else:
                    if self.rank[root_a] == self.rank[root_b]:
                        self.rank[root_b] += 1
                    self.parent[root_a] = root_b
                
                return False
        
        dsu = DSU(len(edges))
        
        for a, b in edges:
            if dsu.union(a,b):
                return [a,b]
