from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.val == other.val
        else:
            return self.val == other

class SinglyLinkedList:
    def __init__(self, head: ListNode = None):
        self.head = head
        self.current = self.head
        self.resize()

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            if self.head is None and other.head is None:
                return True
            if self.size == other.size:
                current_self = self.head
                current_other = other.head
                while current_self is not None:
                    if current_self.val != current_other.val:
                        return False
                    current_self = current_self.next
                    current_other = current_other.next
                return True
        else:
            if self.head is None and not other:
                return True
            if self.size == 1:
                return self.head == other
            if self.size == len(other):
                current = self.head
                for o in other:
                    if o != current:
                        return False
                    current = current.next
                return True
        return False
    
    def __hash__(self) -> int:
        if self.head is None:
            return 0
        else:
            return hash(tuple(self.toArray()))

    def size(self):
        """
        Returns the number of elements in this collection.
        """
        return self.size
    
    def resize(self):
        """
        Counts the number of elements in this collection,
        and set `self.size` atribute.
        """
        if self.head is None:
            self.size = 0
        else:
            self.size = 1
            current = self.head
            while current.next is not None:
                self.size+=1
                current = current.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.head
            raise StopIteration
        else:
            i = self.current.val
            self.current = self.current.next
            return i

    def toArray(self) -> Optional[list]:
        """
        Returns an array containing all of the elements in this collection.
        If this collection makes any guarantees as to what order its elements are returned by its iterator,
        this method must return the elements in the same order.

        The returned array will be "safe" in that no references to it are maintained by this collection.
        (In other words, this method must allocate a new array even if this collection is backed by an array).
        The caller is thus free to modify the returned array. 
        """
        if self.head is None:
            return None
        else:
            return [i for i in self]

    def add(self, e) -> bool:
        """
        Ensures that this collection contains the specified element.
        Returns true if this collection changed as a result of the call.
        (Returns false if this collection does not permit duplicates and already contains the specified element.)

        Collections that support this operation may place limitations on what elements may be added to this collection.
        In particular, some collections will refuse to add null elements,
        and others will impose restrictions on the type of elements that may be added.
        Collection classes should clearly specify in their documentation any restrictions on what elements may be added.

        If a collection refuses to add a particular element for any reason other than that it already contains the element,
        it must throw an exception (rather than returning false).
        This preserves the invariant that a collection always contains the specified element after this call returns.
        """
        if self.head is None:
            self.head = ListNode(e)
            self.current = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = ListNode(e)
        self.size += 1
        return True

    def addAll(self, collection) -> bool:
        """
        Adds all of the elements in the specified collection to this collection.
        The behavior of this operation is undefined if the specified collection is modified while the operation is in progress.
        (This implies that the behavior of this call is undefined if the specified collection is this collection,
        and this collection is nonempty.)
        """
        for e in collection:
            self.add(e)
        return True
    
    def clear(self):
        """
        Removes all of the elements from this collection.
        The collection will be empty after this method returns.
        """
        self.head = None
        self.current = self.head
        self.size = 0
        
    def contains(self, o) -> bool:
        """
        Returns true if this collection contains all of the elements in the specified collection.
        """
        current = self.head
        while current:
            if current.val == o:
                return True
            current = current.next
        return False

    def containsAll(self, iterable) -> bool:
        """
        Returns true if this collection contains all of the elements in the specified collection.
        """
        if self.head is None:
            return False
        for o in iterable:
            if not self.contains(o):
                return False
        return True

    def isEmpty(self) -> bool:
        """
        Returns true if this collection contains no elements.
        """
        return self.head is None

    def equals(self, o) -> bool:
        """
        Compares the specified object with this collection for equality. 
        """
        return self == o
        
    def hashCode(self) -> int:
        """
        Returns the hash code value for this collection. 
        """
        return hash(self)
    
    def __repr__(self):
        return str(self.toArray()) + f"\nSize: {self.size}"
    
    def remove(self, o) -> bool:
        """
        Removes a single instance of the specified element from this collection, if it is present.
        More formally, removes an element e such that (o==null ? e==null : o.equals(e)),
        if this collection contains one or more such elements.
        Returns true if this collection contained the specified element
        (or equivalently, if this collection changed as a result of the call).
        """
        if self.head is None:
            return False
    
        if self.head == o:
            self.head = self.head.next
            self.resize()
            return True
    
        current = self.head
        while current.next is not None:
            if current.next.val == o:
                current.next = current.next.next
                self.resize()
                return True
            current = current.next
        return False
        
    def removeAll(self, collection) -> bool:
        """
        Removes all of this collection's elements that are also contained in the specified collection.
        After this call returns, this collection will contain no elements in common with the specified collection.
        """
        if self.head is None:
            return False
        resize()
        return True

    def removeIf(self, predicate) -> bool:
        """
        Removes all of the elements of this collection that satisfy the given predicate.
        Errors or runtime exceptions thrown during iteration or by the predicate are relayed to the caller.
        """
        if self.head is None:
            return False
        resize()
        return True

    def retainAll(self, collection) -> bool:
        """
        Retains only the elements in this collection that are contained in the specified collection (optional operation).
        In other words, removes from this collection all of its elements that are not contained in the specified collection.
        """
        pass