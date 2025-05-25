from collections import defaultdict

# Time O( N log N)
# Space O(N)
class Solution:
    # identify the connected components -> Union Find
    # sort their indexes, based on the lexicographical order
    # reconstruct the string
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(s) < 2 or len(pairs) < 1:
            return s
            
        # 3 dimentions
        # parent -> component
        # index -> index
        # order 
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [1] * n
            
            def find(self, node):
                # find root
                root = node
                while root != self.parent[root]:
                    root = self.parent[root]
                # path compression opt, mv all node in the path
                while node != root:
                    old_root = self.parent[node]
                    self.parent[node] = root
                    node = old_root
                
                return root
            
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
                
                return
        # O(N)
        dsu = UnionFind(len(s))
        s_swapped = list(s)
        
        for i_a, i_b in pairs:
            dsu.union(i_a, i_b)
            
        # i, letter, but I can't sort different components
        component_indexes = defaultdict(list)
        component_letter = defaultdict(list)
        
        # amortized O(1)
        for i in range(len(s)):
            dsu.find(i)
            
        for s_index, component in enumerate(dsu.parent):
            component_indexes[component].append(s_index)
            component_letter[component].append(s[s_index])
        
        
        # N LOG N
        for component in component_letter:
            indexes = component_indexes[component]
            # N LOG N
            component_letter[component].sort()
            # N
            for i in range(len(indexes)):
                s_swapped[indexes[i]] = component_letter[component][i]
                
            
        # N
        return "".join(s_swapped)
            
            
            
                
                    