# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        n, tail = self.lengthofLL(head)
        if n==0:
            return None
        tail.next = head
        k = k%n
        pivot = n-k-1
        new_tail = head
        for _ in range(pivot):
            new_tail = new_tail.next
            
        # 4. Break the ring
        new_head = new_tail.next
        new_tail.next = None
        return new_head
        
    
    def lengthofLL(self,head):
        n = 0
        curr = head
        prev = None
        while curr:
            n+=1
            prev = curr
            curr = curr.next
        return n, prev
