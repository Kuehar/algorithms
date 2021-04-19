# Time and space complexity O(N) where n is the number of nodes in the list

def reverse_linked_list(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())

# 1 -> 4 -> 2 -> 7
# 7 -> 2 -> 4 -> 1