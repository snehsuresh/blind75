"""
Reorder Linked List
Solved 
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""

from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Step 1 : Find the mid node
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next

        # Step 2 : reverse the second half (recursive)
        slow.next = None  # break the entire list into 2

        def reverse_list(head):
            # newHead = head
            # if head.next:
            #     newHead = reverse_list(head.next)
            #     head.next.next = head
            # head.next = None
            # return newHead
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        reverse_half = reverse_list(second_half)

        # Step 3: Arrage as required
        def arrange_list(list1, list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = arrange_list(next1, next2)
            return list1

        output = arrange_list(head, reverse_half)
        print_linked_list(output)


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
    input_values1 = [1]
    head1 = create_linked_list(input_values1)

    # Print the original linked list
    print("Original linked list (Example 1):")
    print_linked_list(head1)

    # Reorder the linked list using the Solution class
    solution = Solution()
    solution.reorderList(head1)

    # Print the reordered linked list
    print("Reordered linked list (Example 1):")
    print_linked_list(head1)

    # Create another linked list for the second example
    input_values2 = [2, 4, 6, 8, 10]
    head2 = create_linked_list(input_values2)

    # Print the original linked list
    print("Original linked list (Example 2):")
    print_linked_list(head2)

    # Reorder the linked list using the Solution class
    solution.reorderList(head2)

    # Print the reordered linked list
    print("Reordered linked list (Example 2):")
    print_linked_list(head2)
