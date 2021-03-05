# singly linked list is a data structure that it contains objects in a linear order.


class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

    # Search for a key in linked list. Time complexity O(N)
    def search_list(L: ListNode, key: int) -> ListNode:
        while L and L.data != key:
            L = L.next
        # if key wasn't present in the list. L will have become null.
        return L

    # Insert a new node after specified node. Time complexity O(1)
    def insert_node(node: ListNode,new_node: ListNode) -> None:
        new_node.next = node.next
        node.next = new_node
    
    # Delete a node. Time complexity O(1)
    def delete_node(node: ListNode) -> None:
        node.next = node.next.next


    
