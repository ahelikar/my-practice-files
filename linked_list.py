
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
def traverse_print(head):
    currentNode= head
    while currentNode:
        print(currentNode.data,end="->")
        currentNode=currentNode.next
    print("null")
node1=Node(7)
node2=Node(10)
node3=Node(11)
node4=Node(12)
node1.next=node2
node2.next=node3
node3.next=node4
traverse_print(node1)
