"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# generateMock()
# {og1: mock1, og2: mock2}
# mock1 : [mock2]
# og1 : [og2, og4]
# generateMock(og2) -> mock2
# generateMock(og4) -> mock4
# {og1: mock1, og2: mock2, og4: mock4}
# mock1 : [mock2, mock4]

# og4 : [og3, og1]
# generateMock(og3) -> mock3
# {og1: mock1, og2: mock2, og: mock3}
# mock4 : [mock1, mock3]


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        og_to_mock = {}
        visited_nodes = set()
        
        def dfs_clone_graph(node):
            if node in visited_nodes:
                return
            
            if node not in og_to_mock:
                og_to_mock[node] = Node(node.val)
            
            for neigh in node.neighbors:
                if neigh not in og_to_mock:
                    og_to_mock[neigh] = Node(neigh.val)
                # creating connections for mock node
                og_to_mock[node].neighbors.append(og_to_mock[neigh])

            # after creating all conections cur node is done
            visited_nodes.add(node)
            
            # calling the recursive dfs in all neighbors
            for neigh in node.neighbors:
                dfs_clone_graph(neigh)


        dfs_clone_graph(node)
        return og_to_mock[node]

        
        