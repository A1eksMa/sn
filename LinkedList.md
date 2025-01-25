# Definition for singly-linked list
## Python3
### Definition
```python3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
Customizate `__repr__` method to print linked list
```python3
    def __repr__(self):
        next_id = id(self.next) if self.next else None
        return (f"Node: {id(self)}\n({self.val},   {next_id})\n\n"
                + (f"{self.next.__repr__()}" if self.next else ""))
```
Now that looks like a list of nodes
```
Node: id
(val,   next)
```







### Iterator
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

```python3
class ListNodeIterator:
    def __init__(self, head):
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
