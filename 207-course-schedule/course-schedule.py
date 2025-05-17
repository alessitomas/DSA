# 3 ways of representing a graph

# adjancency list
# matrix
# objects and pointers

class Solution:
    class GraphNode:
        def __init__(self):
            self.next = []
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        index_to_node = {}
        
        for course_index, req_index in prerequisites:
            # if course node is not yet, initialized
            if course_index not in index_to_node:
                index_to_node[course_index] = self.GraphNode()
            # if req node is not yet, initialized
            if req_index not in index_to_node:
                index_to_node[req_index] = self.GraphNode()
            
            # lets connect the node through pointers
            index_to_node[course_index].next.append(index_to_node[req_index])

        def dfs_cycle_detection(cur_node, stack_visited, completed_courses):
            # cycle base case
            if cur_node in stack_visited:
                return True
            # was alredy marked as completed base case
            if cur_node in completed_courses:
                return False
            
            stack_visited.add(cur_node)
            
            # all requisites
            for req in cur_node.next:
                has_cycle = dfs_cycle_detection(req, stack_visited, completed_courses)
                
                if has_cycle:
                    return True

            # no req has cycle
            stack_visited.remove(cur_node)
            completed_courses.add(cur_node)
            return False
        
        completed_courses = set()
        for node in index_to_node.values():
            has_cycle = dfs_cycle_detection(node, set(), completed_courses)
            if has_cycle:
                return False
        
        return True
        





        