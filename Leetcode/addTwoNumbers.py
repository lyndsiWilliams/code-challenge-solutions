# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # Reference the previous node, set it as the result, and set it as a blank ListNode
    prev = result = ListNode(None)
    # This will "carry" the values and accumulate the list sums
    # Then it'll be used to handle values past 10
    carry = 0
    
    # while l1, l2, and carry hold uncalculated values:
    while l1 or l2 or carry:
        # If l1 holds an uncalculated value:
        if l1:
            # Add the carry value to l1's value
            carry += l1.val
            # Go to l1's next node
            l1 = l1.next
        # If l2 holds an uncalculated value:
        if l2:
            # Add the carry value to l2's value
            carry += l2.val
            # Go to l2's next node
            l2 = l2.next
            
        # Set the previous node's next to be the remainder of the value once divided by 10
        prev.next = ListNode(carry % 10)
        # "Carry the 10", by setting that remainder value to prev
        prev = prev.next
        # Divide carry by 10 to remove the value we just left in the prev
        carry //= 10
        
    # Return the result's next
    # Which will be the current node, since we set it to prev earlier
    print(result.next)
    return result.next

l1 = [2,4,3]
l2 = [5,6,4]

addTwoNumbers(l1, l2)