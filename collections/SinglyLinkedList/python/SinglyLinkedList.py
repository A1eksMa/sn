class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self, head: ListNode):
        self.current = head

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
