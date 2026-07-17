# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            current = l1.val+ l2.val + carry
            val = current % 10
            carry = current//10
            node= ListNode(val)
            cur.next = node
            cur = cur.next
            l1= l1.next
            l2= l2.next
        
        while l1:
            current = carry + l1.val
            val = current % 10 
            carry = current//10
            node = ListNode(val)
            cur.next = node
            cur= cur.next
            l1= l1.next

        while l2:
            current = carry + l2.val
            val = current% 10
            carry = current //10
            node = ListNode(val)
            cur.next = node
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next



        