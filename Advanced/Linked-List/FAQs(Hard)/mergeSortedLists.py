# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Compare nodes and "sew" the lists together
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # 3. If one list is longer, attach the remainder
        curr.next = list1 if list1 else list2
        
        # 4. Return the next node after dummy (the real head)
        return dummy.next





            
