"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newcopy={None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            newcopy[cur]= copy
            cur = cur.next

        cur = head

        while cur:
            copy= newcopy[cur]
    

            copy.next= newcopy[cur.next]
            copy.random= newcopy[cur.random]

            cur= cur.next

        return newcopy[head]



        