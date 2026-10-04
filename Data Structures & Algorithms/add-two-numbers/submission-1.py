# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = ListNode()
        curr = head

        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            temp = ListNode(sum)
            curr.next = temp
            curr = temp
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            if sum > 9:
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            temp = ListNode(sum)
            curr.next = temp
            curr = temp
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            if sum > 9:
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            temp = ListNode(sum)
            curr.next = temp
            curr = temp
            l2 = l2.next

        if carry == 1:
            curr.next = ListNode(1)

        return head.next
