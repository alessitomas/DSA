# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""



1 - 2 - 3 - 4 - 5

k = 2

4 - 5 - 1 - 2 - 3 


node_count = 5
k = 2

iter = 3

1 - 2 - 3  4 - 5


4 - 5 - 1 - 2 - 3 

Solution 1:

Get the length of the ll
Get the number of rotations needed discarding full rotations

separate the last k nodes from the start of the linked list

cocant the last k node before the start segment

T: O(N)
S: O(1)

"""




class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
            
        node = head
        node_count = 0
        
        while node:
            node_count += 1
            node = node.next

        k %= node_count

        if node_count <= 1 or k == 0:
            return head

        # if node_count <= 1:
        #     return head
        
        prefix_tail = head
        
        for _ in range(node_count - k - 1):
            prefix_tail = prefix_tail.next

        suffix_head = prefix_tail.next 
        prefix_tail.next = None

        suffix_tail = suffix_head
        
        while suffix_tail.next != None:
            suffix_tail = suffix_tail.next

        suffix_tail.next = head
        return suffix_head

        

        cur = new_


        








        
        