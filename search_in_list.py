def search_list(L: ListNode,key: int) -> ListNode:
  while L and L.data != key:
    L = L.next
  # If key was not present in the list, L will have become null.
  return L
