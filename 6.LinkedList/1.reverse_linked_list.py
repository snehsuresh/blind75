"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]

"""

from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative solution
        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

        # Recursive solution
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print the linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)


# Example usage
if __name__ == "__main__":
    # Create a linked list from a list of values
    input_values = [0, 1, 2, 3]
    head = create_linked_list(input_values)

    # Print the original linked list
    print("Original linked list:")
    print_linked_list(head)

    # Reverse the linked list using the Solution class
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Print the reversed linked list
    print("Reversed linked list:")
    print_linked_list(reversed_head)
