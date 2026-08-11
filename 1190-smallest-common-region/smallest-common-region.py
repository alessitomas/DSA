"""
if x -> y and y ->  z then x => z

relationships can be mapped as a DAG

A <- B <- C desing is better because we know the sources and it's guaranteed that the first node visited twice is the closest 

where A contains B that contains C

design the graph

Dual origin BFS as soon as the same node is visited twice we have the closest parent 

BFS

O(V + E)
S(V)

UNION FIND to explore ?

"""

from collections import deque, defaultdict

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        # adjacency list
        regions_graph = defaultdict(list)

        for row in regions:
            for region in row:
                regions_graph[region].append(row[0])

        print(regions_graph)

        def get_closest_parent_region(src_a, src_b):
            visited = {src_a: 1, src_b: 2} # "1" by region 1 "2" by region 2 
            queue = deque([src_a, src_b])


            while len(queue) > 0:
                cur = queue.popleft()


                for parent in regions_graph[cur]:
                    if parent in visited and visited[parent] == visited[cur]:
                        continue 
                    
                    if parent in visited and visited[parent] != visited[cur]:
                        return parent

                    queue.append(parent)
                    visited[parent] = visited[cur]

        
        closest_region = get_closest_parent_region(region1, region2)
        return closest_region











        