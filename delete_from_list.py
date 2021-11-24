# Delete the node past this one. Assume node is not a tail.
def delete_after(node:ListNode) -> None:
  node.next = node.next.next
