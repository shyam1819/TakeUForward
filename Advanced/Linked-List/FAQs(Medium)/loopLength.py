# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        slow = self.findLoop(head)
        if slow is None:
            return 0
        fast = slow
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count+=1
            if slow==fast:
                return count

    def findLoop(self,head):
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
