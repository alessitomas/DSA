class Solution:
    def union_find(self, n, edges):
        # space (V)
        # Time O(E * a(N)), where a(N) is inverse ackermann function, could be considered constant
        class DSU:
            def __init__(self, n):
                self.cc = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
            def find(self, node):
                # find root
                root = node
                while root != self.parent[root]:
                    root = self.parent[root]
                
                # mv all node in path
                while node != root:
                    old_root = self.parent[node]
                    self.parent[node] = root
                    node = old_root
                
                return root
                    
            def union(self, node_a, node_b):
                root_a = self.find(node_a)
                root_b = self.find(node_b)
                
                if root_a == root_b:
                    return 
                
                if self.rank[root_a] >= self.rank[root_b]:
                    self.parent[root_b] = root_a
                    if self.rank[root_a] ==  self.rank[root_b]:
                        self.rank[root_a] += 1
                else:
                    self.parent[root_a] = root_b
                    
                self.cc -= 1
        
        dsu = DSU(n)
        for node_a, node_b in edges:
            dsu.union(node_a, node_b)
        
        return dsu.cc
        
                
                        
                    
                
        
    
    from collections import defaultdict, deque
    # Space: O(V + E)
    # Time: O(E)
    def create_adjacency_list_from_edge_list(self, edges):
        adjacency_list = defaultdict(list)
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        return adjacency_list
        
    # Space: O(V + E)
    # Time: O(V + E)
    def bfs(self, n, edges):
        adjacency_list = self.create_adjacency_list_from_edge_list(edges)
        visited = set()
        
        def bfs_exploration(cur_index):
            queue = deque([cur_index])
            visited.add(cur_index)
            
            while len(queue) > 0:
                cur_index = queue.popleft()
                for neigh in adjacency_list[cur_index]:
                    if neigh in visited:
                        continue
                    queue.append(neigh)
                    visited.add(neigh)  
            return 
        
        cc = 0
        # Time: O(V)
        for i in range(n):
            if i not in visited:
                cc += 1
                bfs_exploration(i)
        
        return cc
    
    # Space: O(V + E)
    # Time: O(V + E)
    def dfs_iter(self, n, edges):
        adjacency_list = self.create_adjacency_list_from_edge_list(edges)
        visited = set()
        
        def dfs_exploration(cur_index):
            stack_call = [cur_index]
            visited.add(cur_index)
            
            while len(stack_call) > 0:
                cur_index = stack_call.pop(-1)
                for neigh in adjacency_list[cur_index]:
                    if neigh in visited:
                        continue
                    stack_call.append(neigh)
                    visited.add(neigh)  
            return 
        
        cc = 0
        # Time: O(V)
        for i in range(n):
            if i not in visited:
                cc += 1
                dfs_exploration(i)
        
        return cc
    
    # Space: O(V + E)
    # Time: O(V + E)
    def dfs_rec(self, n, edges):
        # Space: O(V + E)
        # Time: O(E)
        adjacency_list = self.create_adjacency_list_from_edge_list(edges)
        # Space: O(V)
        visited = set()
        
        # Time: O(V + E)
        # Space: O(V)
        def dfs_exploration(cur_index):
            if cur_index in visited:
                return
            
            visited.add(cur_index)
            
            for neigh in adjacency_list[cur_index]:
                dfs_exploration(neigh)
            
            return    
            
        cc = 0
        # Time: O(V)
        for i in range(n):
            if i not in visited:
                cc += 1
                dfs_exploration(i)
        
        return cc
                
                
    
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.union_find(n, edges)
        
        