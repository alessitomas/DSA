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
# time O(N + V)
# space O(N)
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        og_to_mock = {}
        visited_nodes = set()

        def bfs_traversal(node):
            og_to_mock[node] = Node(node.val)
            
            queue = deque([node])
            visited_nodes.add(node)

            while len(queue) > 0:
                cur_node = queue.popleft()
                for neigh in cur_node.neighbors:
                    if neigh not in og_to_mock:
                        og_to_mock[neigh] = Node(neigh.val)
                    
                    og_to_mock[cur_node].neighbors.append(og_to_mock[neigh])
                    if neigh not in visited_nodes:
                        queue.append(neigh)
                        visited_nodes.add(neigh)

        bfs_traversal(node)
        return og_to_mock[node]

        
        