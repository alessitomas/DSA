# a / b = 2
# num / div = q 

# num = q * div
# {num : {div : 1 / q}}
# num = q * div
# {div : {num : 1 * q}}

# {a : {b: 1 / 2}}
# {b : {a: 2}}

# b / c = 3

# {b : {c: 1 / 3}}
# {c : {b: 3}}

# a / c
# find a common key between a and c and divide else return -1


# model as a graph problem
# if there is a relation they must be connected

# there are relations between division
# A / B = c

# A -> B is 1 / c 
# B -> A is 1 * c 

# A <-> B <-> C

# A -> 

# To calculate A / C, it is neede to traverse the relations graph from A to C calculating # the amount. If there is no connection return -1.


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class GraphNode:
            def __init__(self):
                self.neighboors = []
                self.weights = []
        
        node_map = {}
        
        for (num, div), res in zip(equations, values):
            if num not in node_map:
                node_map[num] = GraphNode()
            if div not in node_map:
                node_map[div] = GraphNode()
            # num -> div
            node_map[num].neighboors.append(node_map[div])
            node_map[num].weights.append(res)
            # num -> div
            node_map[div].neighboors.append(node_map[num])
            node_map[div].weights.append(1/res)
        
        results = []
        
        def dfs_traversal(cur_node, target_node, cur_amount, visited, NO_RESULT):
            if cur_node in visited:
                return NO_RESULT
            if cur_node == target_node:
                return cur_amount
            
            visited.add(cur_node)
            
            for neigh, weight in zip(cur_node.neighboors, cur_node.weights):
                res = dfs_traversal(neigh, target_node, cur_amount * weight, visited, NO_RESULT)
                if res != NO_RESULT:
                    return res
            
            return NO_RESULT

        NO_RESULT = None
        for num, div in queries:
            if num not in node_map or div not in node_map:
                results.append(-1)
            else:
                res = dfs_traversal(node_map[num], node_map[div], 1, set(), NO_RESULT)
                if res == NO_RESULT:
                    results.append(-1)
                else:
                    results.append(res)

        return results

