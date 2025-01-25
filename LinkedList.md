# Definition for singly-linked list.
```python3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

```php
class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val) { $this->val = $val; }
}
```

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
