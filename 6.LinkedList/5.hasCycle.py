from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while (
            slow and fast and fast.next
        ):  # because if fast.next is None, fast.next.next will raise an AttributeError
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Helper function to create a linked list from a list of values and add a cycle based on the index
def create_linked_list_with_cycle(values, index):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]

    # Create the rest of the list
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)

    # If the index is valid, create a cycle
    if index != -1:
        current.next = nodes[index]

    return head


# Helper function to print the linked list (will stop if a cycle is detected)
def print_linked_list(head):
    values = []
    current = head
    visited = set()

    while current:
        if current in visited:
            values.append(f"Cycle detected at node with value: {current.val}")
            break
        visited.add(current)
        values.append(current.val)
        current = current.next

    print(values)


# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle based on the index
    input_values = [1, 2, 3, 4]
    cycle_index = 1  # Create a cycle starting at index 1 (node with value 2)
    head = create_linked_list_with_cycle(input_values, cycle_index)

    # Print the linked list (will detect if a cycle exists)
    print("Linked list with potential cycle:")
    print_linked_list(head)

    # Check if the linked list has a cycle using the Solution class
    solution = Solution()
    has_cycle = solution.hasCycle(head)
    print(f"Has cycle: {has_cycle}")

    # Example with no cycle
    input_values_no_cycle = [1, 2, 3, 4]
    head_no_cycle = create_linked_list_with_cycle(input_values_no_cycle, -1)  # No cycle

    print("\nLinked list without cycle:")
    print_linked_list(head_no_cycle)

    # Check if the linked list without a cycle has a cycle
    has_cycle_no_cycle = solution.hasCycle(head_no_cycle)
    print(f"Has cycle (no cycle case): {has_cycle_no_cycle}")
