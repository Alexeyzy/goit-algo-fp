# Однозвязний список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")

llist = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Однозвязний список:")
llist.print_list()



        
# Реверсування однозв'язного списку
def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    linked_list.head = prev

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

print("Початковий список:")
llist.print_list()

reverse_linked_list(llist)
print("Реверсований список:")
llist.print_list()



# Сортування однозв'язного списку
def merge_sort_linked_list(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next
    middle.next = None

    left = LinkedList()
    left.head = linked_list.head
    right = LinkedList()
    right.head = next_to_middle

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    sorted_list = LinkedList()
    sorted_list.head = merge_sorted_lists(left.head, right.head)
    return sorted_list

def get_middle(node):
    if not node:
        return node

    slow, fast = node, node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, left.next)
    return result

llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)

print("Початковий список:")
llist.print_list()

sorted_llist = merge_sort_linked_list(llist)
print("Відсортований список:")
sorted_llist.print_list()






