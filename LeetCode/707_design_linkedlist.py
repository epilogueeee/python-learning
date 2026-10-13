class Node:
    def __init__(self, val):
        
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        p = self.head.next
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:

        newNode = Node(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.prev.next = newNode
        newNode.next.prev = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:

        newNode = Node(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        newNode.prev.next = newNode
        newNode.next.prev = newNode
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index >= self.size:
            return -1

        newNode = Node(val)
        p = self.head.next
        for _ in range (index):
            p = p.next
        newNode.prev = p.prev
        newNode.next = p
        newNode.prev.next = newNode
        newNode.next.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return -1
        
        p = self.head.next
        for _ in range(index):
            p = p.next
        p.prev.next = p.next
        p.next.prev = p.prev
        p.prev = None
        p.next = None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)