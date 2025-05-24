from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        if n == 0: return True

        graph_adjc_list = defaultdict(list)
        
        for node_a, node_b in edges:
            graph_adjc_list[node_a].append(node_b)
            graph_adjc_list[node_b].append(node_a)
            
        visited = set()
        
        def dfs_detecting_cycle(cur_node, parent):
            if cur_node in visited:
                return True
            
            visited.add(cur_node)

            for neigh in graph_adjc_list[cur_node]:
                if neigh == parent:
                    continue 

                if dfs_detecting_cycle(neigh, cur_node):
                        return True
            
            return False


        return not dfs_detecting_cycle(0, None) and len(visited) == n