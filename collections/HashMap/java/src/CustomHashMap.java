//import java.util.AbstractMap;
//import java.util.Map;
//import java.util.Set;


public class CustomHashMap<K,V> {//extends AbstractMap<K,V> implements Map<K,V> {
    private int size;
    private int resizeFactor;


    public CustomHashMap(int resizeFactor) {
        this.size = 0;
        this.resizeFactor = resizeFactor;
    }
    
    public static int calculateIndex(Object e, int l) {
        int h = e.hashCode();
        long min_int = Integer.MIN_VALUE;
        long max_int = Integer.MAX_VALUE;
        float r = (float)((long) h - min_int) / (max_int - min_int);
        int i = Math.round((float) (l - 1) * r);
        return i;
    }
}