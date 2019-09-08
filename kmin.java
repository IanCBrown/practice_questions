import java.util.Arrays;

public kmin {

    public static void main(String[] args) {


    }


    /**
    * Selects the kth minimum value from the array a. This method
    * throws IllegalArgumentException if a is null, has zero length,
    * or if there is no kth minimum value. Note that there is no kth
    * minimum value if k < 1, k > a.length, or if k is larger than
    * the number of distinct values in the array. The array a is not
    * changed by this method.
    */
    public static int kmin(int[] a, int k) {
        if (a == null || a.length == 0 || k < 1 || k > a.length) {
           throw new IllegalArgumentException();
        }
     
        int[] sorted = Arrays.copyOf(a, a.length);
        Arrays.sort(sorted);
     
        if (k == 1) {
           return sorted[0];
        }
     
        int value = 0;
        int kCount = 1;
        for (int i = 1; i < sorted.length; i++, value++) {
           if (sorted[i] != sorted[value]) {
              kCount++;
              if (kCount == k) {
                 return sorted[i];
              }
           }
        }
     
        if (k > kCount) {
           throw new IllegalArgumentException();
        }
        return k;
     }


    /**
    * Selects the kth minimum value from the array a. This method
    * throws IllegalArgumentException if a is null, has zero length,
    * or if there is no kth minimum value. Note that there is no kth
    * minimum value if k < 1, k > a.length, or if k is larger than
    * the number of distinct values in the array. The array a is not
    * changed by this method.
    */
     public static int kmin(int[] a, int k) {
        if (a == null || a.length == 0 || k < 1 || k > a.length) {
           throw new IllegalArgumentException();
        }
     
        int[] sorted = Arrays.copyOf(a, a.length);
        Arrays.sort(sorted);
     
        int value = 1;
        int kCount = 1;
        for (int i = 0; i < sorted.length; i++, value++) {
           if (sorted[i] != sorted[value]) {
              kCount++;
              if (kCount == k) {
                 return sorted[i];
              }
           }
        }
     
        if (k > kCount) {
           throw new IllegalArgumentException();
        }
        return k;
     }

}
   
  