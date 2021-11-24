# Insert new_node after node.
def insert_after(node: ListNode, new_node: ListNode) -> None:
  new_node.next = node.next
  node.next = new_node
