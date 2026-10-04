"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        curr = head

        # Inserting new nodes next to every Node in original Linked List
        # And next pointers are set
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        curr = head

        # Connecting Randoms
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = curr.next
        # Seperate copy and original list

        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = curr.next.next
            curr = curr.next
        return copy_head
