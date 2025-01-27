import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class E_LinkedListIteratorTest {

    @Test
    public void E_LinkedListIterator() {
        String one = "One";
        String two = "Two";
        String three = "Three";
        
        // Test E_LinkedList class
        E_LinkedList<String> e_linked_list = new E_LinkedList<>();

        // Test `.add()` method of E_LinkedList class
        e_linked_list.add(one);
        e_linked_list.add(two);
        e_linked_list.add(three);
        
        // Test `.iterator()` method of E_LinkedList class
        for (String e: e_linked_list) {
            System.out.println(e);
        }

        // Проверяем, что элемент больше не существует
            assertFalse(list.remove("ABCD"), "Элемент уже был удалён, удаление должно вернуть false");
    }
}