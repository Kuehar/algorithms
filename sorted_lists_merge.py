def merge_two_sorted_lists(L1,L2):
    # creates a placehoder for the list
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next,L1 = L1,L1.next
        else:
            tail.next,L2 = L2,L2.next
    # Appends the remaining nodes of L1 and L2
    tail.next = L1 or L2
    return dummy_head.next