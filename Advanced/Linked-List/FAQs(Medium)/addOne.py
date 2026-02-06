class Solution:
    def addOne(self, head):
        # Helper to reverse the list
        def reverse(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # 1. Reverse
        head = reverse(head)
        
        # 2. Add one
        curr = head
        carry = 1
        while curr and carry:
            new_val = curr.val + carry
            carry = new_val // 10
            curr.val = new_val % 10
            
            if carry and not curr.next:
                curr.next = ListNode(0) # Make room for final carry
            curr = curr.next
            
        # 3. Reverse back
        return reverse(head)
