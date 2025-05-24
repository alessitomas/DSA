class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
            
            def find(self, a):
                a_parent = self.parent[a]
                if a_parent != a:
                    self.parent[a] = self.find(a_parent)
                    return self.parent[a]
                return a_parent
            
            def union(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)
                
                if root_a == root_b:
                    return 
                
                if self.rank[root_a] > self.rank[root_b]:
                    self.parent[root_b] = root_a
                else: 
                    self.parent[root_a] = root_b
                    
                if self.rank[root_a] == self.rank[root_b]:
                    self.rank[root_b] += 1
            
            def connect(self, a, b):
                return self.find(a) == self.find(b)
        
        
        dsu = UnionFind(len(isConnected))
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    dsu.union(i,j)
                    
        
        roots_seen = set()
        for i in range(len(isConnected)):
            roots_seen.add(dsu.find(i))
        return len(roots_seen)
            
                    
                    
                
        