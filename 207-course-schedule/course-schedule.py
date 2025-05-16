class Solution:
    class Graph:
        def __init__(self, val):
            self.val = val
            self.adjacent = []
    
    def dfs_exploration(self, cur_node, visited, seen):
        if cur_node in visited:
            return False
        if cur_node in seen:
            return True
        visited.add(cur_node)
        
        
        for req in cur_node.adjacent:
            if not self.dfs_exploration(req, visited, seen):
                return False
        visited.remove(cur_node)
        seen.add(cur_node)
        return True


    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        for course_req in prerequisites:
            course = course_req[0]
            req = course_req[1]

            if not course in nodes:
                nodes[course] = self.Graph(course)
            if not req in nodes:
                nodes[req] = self.Graph(req)

            nodes[course].adjacent.append(nodes[req])
        
        seen = set()
        
        for node in nodes.values():
            if not node in seen:
                if not self.dfs_exploration(node, set(), seen):
                    return False

        return True


        

            

        