# Time Complexity: O(n)
# Space Complexity: O(1)
203. Remove Linked List Elements

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        current_node = dummy_head

        while current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next


707. Design Linked List
class Node:
    def __init__(self, val, next_node:'Node' = None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head:Node = None
        self.length:int = 0

    def get(self, index: int) -> int:
        # Validate index: must be within [0, length-1]
        if not isinstance(index, int) or index < 0 or index >= self.length:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -=1
        return curr.val      

    def addAtHead(self, val: int) -> None:
        self.head: Node = Node(val, self.head) 
        self.length += 1
        return

    def addAtTail(self, val: int) -> None:
        # Handle empth linked list
        if self.length == 0:
            self.addAtHead(val)
            return None
        # Traverse to the tail node
        curr = self.head
        for _ in range(self.length-1):
            curr = curr.next
        curr.next = Node(val, None)
        self.length += 1
        return None   

    def addAtIndex(self, index: int, val: int) -> None:
        # Handle invalid index
        if not isinstance(index, int) or index < 0 or index > self.length:
            return None
        #Handle at head or at tail
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        # Traverse to the previous node of the inserting index
        pre = self.head
        for _ in range(index -1):
            pre = pre.next
        pre.next = Node(val, pre.next)
        self.length += 1
        return  None

    def deleteAtIndex(self, index: int) -> None:
        # check invalid index
        if not isinstance(index, int) or index < 0 or index >= self.length:
            return None
        # dummy_head -> self.head-> second node or None
        # Traverse to the previous node of the deleting index
        dummy_head = Node(0, self.head)
        pre = dummy_head
        for _ in range(index):
            pre = pre.next
        # Unlink the node
        pre.next = pre.next.next
        # upadte the head incase index == 0
        self.head = dummy_head.next
        self.length -= 1
        return None


206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            # Temporarily store the next node
            tmp = cur.next
            cur.next = prev # Reverse
            # Move prev and curr one step forward
            prev = cur
            cur = tmp
        # prev will be the new head
        return prev


       
24. Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        cur = dummy

        while cur.next and cur.next.next:
            # Store the next 2 nodes
            first = cur.next
            second = cur.next.next
            # Swaping nodes
            cur.next = second
            first.next = second.next
            second.next = first
            # Move forward
            cur = first

        return dummy.next



19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        cur = dummy
        fast = dummy
        # Move fast pointer n+1 steps ahead to maintain a gap of n between fast and cur. When fast reaches end, cur will be at the node before the target
        for _ in range(n+1):
            fast = fast.next
        # Traverse fast to the end.next (fast will point to None after loop)
        while fast:
            cur = cur.next
            fast = fast.next
        cur.next = cur.next.next
        return dummy.next



160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time Complexity: O(m+n)
# Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        # Make listB the longer list
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        # Move curB forward by the difference in lengths to align both lists
        for _ in range(lenB - lenA):
            curB = curB.next
        # Traverse both lists in sync to find intersection
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None


142. Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # found a loop
            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# Time Complexity: O(n)
# Space Complexity: O(n)           
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         visited = set()
#         cur = head
#         while cur:
#             if cur in visited:
#                 return cur
#             visited.add(cur)
#             cur = cur.next
#         return None            
