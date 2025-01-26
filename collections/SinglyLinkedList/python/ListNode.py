class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            result = self.current.val
            self.current = self.current.next
            return result

    def __repr__(self):
        next_id = id(self.next) if self.next else None
        return (f"Node: {id(self)}\n({self.val},   {next_id})\n\n"
                + (f"{self.next.__repr__()}" if self.next else ""))

    @classmethod
    def toListNode(cls, iterable):
        if not iterable:
            return None
        head = cls(iterable[0])
        current = head
        for value in iterable[1:]:
            current.next = cls(value)
            current = current.next
        return head

    def toList(self):
        return [i for i in self]

    def add(self, val):
        current = self
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def addAll(self, iterable):
        current = self
        while current.next:
            current = current.next
        for i in iterable:
            current.next = ListNode(i)
            current = current.next

    def contains(self, val):
        current = self
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def pop(self):
        current = self
        while current.next.next:
            current = current.next
        value = current.next.val
        current.next = None
        return value
