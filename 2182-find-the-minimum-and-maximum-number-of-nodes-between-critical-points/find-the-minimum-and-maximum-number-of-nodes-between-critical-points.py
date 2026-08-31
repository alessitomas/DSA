# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
to be a critial point

1.   ll[i] > ll[i-1] and ll[i] > ll[i+1]
2.   ll[i] < ll[i-1] and ll[i] < ll[i+1]

minDistance: bewtween two consecutive
maxDistance: first to the last one

can be done in O(1) space, since we will only need to store first and last and we can compare consecutives as we go for min
time: O(n), need to visit all nodes onces

"""

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if not head:
            return [-1,-1]
        
        prev = head
        cur = head.next
        cur_idx = 1

        first_critical_point = last_critical_point = -1
        
        min_distance = float("inf")
        max_distance = 0
        
        while cur and cur.next:
            # local minima or local maxima
            # critical point
            if (prev.val > cur.val and cur.next.val > cur.val) or (prev.val < cur.val and cur.next.val < cur.val):
                
                if first_critical_point == -1:
                    first_critical_point = cur_idx
                else:
                    max_distance =  cur_idx - first_critical_point
                    min_distance = min(min_distance, cur_idx - last_critical_point)
                

                last_critical_point = cur_idx
            
            prev = cur
            cur = cur.next
            # FORGOT TO UPDATE INDEX
            cur_idx += 1
        
        print(first_critical_point, last_critical_point)

        if first_critical_point == last_critical_point:
            return [-1,-1]
        
        return [min_distance, max_distance]
                    
                

                    
                


                    
                




        