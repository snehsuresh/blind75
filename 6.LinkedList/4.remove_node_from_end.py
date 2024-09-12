"""
Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
"""


from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pass


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
    # Example 1
    input_values1 = [1, 2, 3, 4]
    n1 = 2
    head1 = create_linked_list(input_values1)

    # Print the original linked list
    print("Original linked list (Example 1):")
    print_linked_list(head1)

    # Remove the nth node from the end of the list using the Solution class
    solution = Solution()
    modified_head1 = solution.removeNthFromEnd(head1, n1)

    # Print the modified linked list
    print("Modified linked list (Example 1):")
    print_linked_list(modified_head1)

    # Additional example
    input_values2 = [1, 2, 3, 4, 5]
    n2 = 1
    head2 = create_linked_list(input_values2)

    # Print the original linked list
    print("Original linked list (Example 2):")
    print_linked_list(head2)

    # Remove the nth node from the end of the list using the Solution class
    modified_head2 = solution.removeNthFromEnd(head2, n2)

    # Print the modified linked list
    print("Modified linked list (Example 2):")
    print_linked_list(modified_head2)
