# Singly-linked list
| [ENG](https://github.com/A1eksMa/sn/blob/main/collections/SinglyLinkedList/SinglyLinkedList.md) | [RU](https://github.com/A1eksMa/sn/blob/main/collections/SinglyLinkedList/SinglyLinkedList_RU.md) |
|head|h|
|current|c|
|value|v|
|next|n|


## Python3
### Definition
Definition for singly-linked list
```python3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
Convert any iterable sequence (list, tuple and other) to singly-linked list
```python3
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
```
Example of usage:
```python3
t = (1,2,3)
head = ListNode.toListNode(t)
```

### Iteration
Create linked list from tupple (as an example above).

Go ahead using `while`
```python3
current = head
while current:
    print(current.val)
    current = current.next
```

Add `__iter__` and `__next__` methods to make class ListNode iterable
```python3
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
```

and go ahead using `for`
```python3
current = head
for i in current:
    print(i)
```

Output values with `while`, `for` will be same:
```python3
>>> 1
>>> 2
>>> 3
```

### Reverse
Using recurcive function
```python3
current = head
def move_backward(n):
    if n is None:
        return
    move_backward(n.next)
    print(n.val)
        
move_backward(current)
```

Output
```python3
>>> 3
>>> 2
>>> 1
```

Add an element to end of linked list
```python3
    def add(self, val):
        current = self
        while current.next:
            current = current.next
        current.next = ListNode(val)
```

Add collections or any iterable sequence to end of linked list
```python3
    def addAll(self, iterable):
        current = self
        while current.next:
            current = current.next
        for i in iterable:
            current.next = ListNode(i)
            current = current.next
```

Checks whether the value exists in list
```python3
    def contains(self, val):
        current = self
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
```

Customizate `__repr__` method to print linked list
```python3
    def __repr__(self):
        next_id = id(self.next) if self.next else None
        return (f"Node: {id(self)}\n({self.val},   {next_id})\n\n"
                + (f"{self.next.__repr__()}" if self.next else ""))
```
Now that looks like a list of nodes. Example of usage:
```
print(head)
>>> Node_1: id        #head
>>> (val,   next)
>>>
>>> Node_2: id
>>> (val,   next)
>>>
>>> Node_3: id
>>> (val,   next)
>>>
```
## java
```java
public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
```
## php
```php
class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val) { $this->val = $val; }
}
```
## rust
```rust

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}
```
