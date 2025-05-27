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

# A = B * c

# A * C-> B
# A = b * 2

# B * C = A 

# B / C -> A


# A -> B is 1 / c 
# B -> A is 1 * c 

# A <-> B <-> C

# A -> 

# To calculate A / C, it is neede to traverse the relations graph from A to C calculating # the amount. If there is no connection return -1.

# Space Complexity: (E + V + Q)
# Time Complexity: (Q * (E + V))





# identifier weight -> x
# a -> 2 x
# b - 3 x


# a / b = 2/3

# union(a,b)
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(defaultdict)
        
        node_map = {}
        
        for (num, div), res in zip(equations, values):
            # num -> div
            graph[num][div] = res
            # div -> num
            graph[div][num] = 1/res
            
        results = []
        
        def dfs_traversal(cur_node, target_node, cur_amount, visited, NO_RESULT):
            if cur_node in visited:
                return NO_RESULT
            if cur_node == target_node:
                return cur_amount
            
            visited.add(cur_node)
            
            for neigh in graph[cur_node]:
                weight = graph[cur_node][neigh]
                res = dfs_traversal(neigh, target_node, cur_amount * weight, visited, NO_RESULT)
                if res != NO_RESULT:
                    return res
            
            return NO_RESULT

        NO_RESULT = None
        for num, div in queries:
            if num not in graph or div not in graph:
                res = -1
            else:
                res = dfs_traversal(num, div, 1, set(), NO_RESULT)
                res = \
                    res if res is not NO_RESULT else -1
            
            results.append(res)

        return results

