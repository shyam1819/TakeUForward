# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        nodes = set()
        while head is not None:
            if head not in nodes:
                nodes.add(head)
                head = head.next
            else:
                return True
        return False
