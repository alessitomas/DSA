# tree does no have cycle
# parent is just connected to its directs sons
# each son only have one parent
# there are no connections between nodes in the same level
# it must be a connected graph

from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class GraphNode:
            def __init__(self, val):
                self.val = val
                self.connections = []
        if n == 1:
            return True
        node_map = {}
        # creating of Graph Nodes
        for nd1, nd2 in edges:
            if nd1 not in node_map:
                node_map[nd1] = GraphNode(nd1)
            if nd2 not in node_map:
                node_map[nd2] = GraphNode(nd2)
            
            node_map[nd1].connections.append(node_map[nd2])
            node_map[nd2].connections.append(node_map[nd1])
        
        def bfs_no_cycle(node, visited):
            queue = deque()
            queue.append((node, None))
            visited.add(node)

            while len(queue) > 0:
                cur_node, parent_node = queue.popleft()

                for connection in cur_node.connections:
                    if connection != parent_node:
                        # cycle case
                        if connection in visited:
                            return False
                        queue.append((connection, cur_node))
                        visited.add(connection)

            return True

        # all nodes
        for i in range(n):
            if i not in node_map:
                return False
            visited_nodes = set()
            ## bfs no cycle
            if bfs_no_cycle(node_map[i], visited_nodes) and len(visited_nodes) == n:
                return True
        return False

        

        