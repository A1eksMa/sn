import unittest
from SinglyLinkedList import ListNode, SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    # Test
    def test_ListNode(self):
        """ Test: iterator. """
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        LinkedList = SinglyLinkedList(head)
        res  =[]
        for node in LinkedList:
            res.append(node)
        self.assertEqual(res, [1,2,3])
          
if __name__ == '__main__':
    unittest.main()
