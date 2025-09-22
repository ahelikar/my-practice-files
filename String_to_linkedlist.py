class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def string_to_linkedlist(s):
    if not s:
        return None:
    head=Node(s[0])
    current=head
    for char in range s[l:]:
        newNode=Node(char)
        current.next=newNode
        current=newNode
    return head
def print_linked_list(head):
    """
    Prints the data of each node in the linked list.
    """
    current = head
    while current:
        print(f"{current.data} -> ", end="")
        current = current.next
    print("None")

my_string = "python"
linked_list_head = string_to_linkedlist(my_string)

print(f"Linked list created from string \"{my_string}\":")
print_linked_list(linked_list_head)

empty_string = ""
empty_list_head = string_to_linkedlist(empty_string)
print("\nLinked list from an empty string:")
print_linked_list(empty_list_head
