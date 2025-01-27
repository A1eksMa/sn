class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self, head: ListNode):
        self.head = head
        self.current = self.head
        self.resize()
        
    def resize(self):
        self.size = 0
        self.current = self.head
        while self.current.next is not None:
            self.size+=1
            current = current.next
        self.current = self.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            result = self.current.val
            self.current = self.current.next
            return result

    def contains(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def containsAll(self, iterable):
        for val in iterable:
            if not self.contains(val):
                return False
        return True

    def remove(self, val):
        current = self.head
        previous = None
        
        while current:
            if current.val == val:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        
        return False

    def isEmpty(self) -> boolean:
        return head is None

    def clear(self):
        pass

    def add(self) -> boolean:
        pass

    def addAll(self) -> boolean
        pass
