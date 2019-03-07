import java.util.Iterator;
import java.util.Random;
import java.util.NoSuchElementException;


/**
 * RandomizedList.java. Describes the abstract behavior of a
 * randomized list collection; that is, a list with order defined as "random
 * order." The order described by a radomized list is "random" in the sense
 * that the element accessed by either the sample or remove method is selected
 * uniformly at random from the current elements in the list. In addition, an
 * iterator on a randomized list will sequentially access each element in some
 * uniformly random sequence. Simultaneous iterators on the same randomized
 * list are independent of each other. That is, they will with high probability
 * have different iteration sequences.
 */

//use Arrays!!
public class ArrayRandomizedList<T> implements RandomizedList<T> {

   public static final int DEFAULT_CAPACITY = 1;

   private T[] elements;

   private int size;


  //////////////////
  // Constructors //
  //////////////////

   public ArrayRandomizedList() {
      this(DEFAULT_CAPACITY);
   }

  /**
   * Construct an ArrayBag of the specified capacity.
   */
   @SuppressWarnings("unchecked")
   public ArrayRandomizedList(int capacity) {
      size = 0;
      elements = (T[]) new Object[capacity];
   }

  //--------------------------------------
  //----Methods from Randomized List------
  //--------------------------------------

  /**
   * Adds the specified element to this list. If the element is null, this
   * method throws an IllegalArgumentException.
   */
   public void add(T element) {
      if (element == null) {
         throw new IllegalArgumentException();
      }
      if (isFull()) {
         resize(size * 2);
      }

      elements[size] = element;
      size++;
   }

  /**
   * Selects and removes an element selected uniformly at random from the
   * elements currently in the list. If the list is empty this method returns
   * null.
   */
   public T remove() {
      if (isEmpty()) {
         return null;
      }

      Random r = new Random();
      int rand = r.nextInt(size);
      T t = elements[rand];

      if (elements.length == 1) {
         elements[0] = null;
      }
      else {
         elements[rand] = elements[size - 1];
         elements[size - 1] = null;
      }
      if (isSparse()) {
         resize(elements.length / 2);
      }
      size--;
      return t;
   }

  /**
   * Selects but does not remove an element selected uniformly at random from
   * the elements currently in the list. If the list is empty this method
   * return null.
   */
   public T sample() {
      if (isEmpty()) {
         return null;
      }
      Random r = new Random();
      int rand = r.nextInt(size);

      return elements[rand];
   }

  //---------------------------
  //----Methods from List------
  //---------------------------

  /**
   * Returns the number of elements in this list.
   */
   public int size() {
      return size;
   }

  /**
   * Returns true if this list contains no elements, false otherwise.
   */
   public boolean isEmpty() {
      return size == 0;
   }

  /**
   * Creates and returns an iterator over the elements of this list.
   */
   public Iterator<T> iterator() {
      return new ArrayIterator(elements, size);
   }

    //---------------------------
    //----Private Methods--------
    //---------------------------

   private boolean isFull() {
      return size == elements.length;
   }

   private boolean isSparse() {
      return (size > 0) && (size < elements.length / 4);
   }

   private void resize(int newSize) {
      assert newSize > 0;
      @SuppressWarnings("unchecked")
         T[] newArray = (T[]) new Object[newSize];
      System.arraycopy(elements, 0, newArray, 0, size);
      elements = newArray;
   }

  ////////////////////
  // Nested classes //
  ////////////////////

   private class ArrayIterator implements Iterator<T> {

    // the array of elements to iterate over
      private T[] elements;
    // the number of elements in the array, beginning at index zero
      private int count;
    // the index of the next element in the iteration sequence
      private int current;

      private int prevRand;

    /**
     * Construct a properly initialized iterator.
     *
     * @param  elem the array to be iterated over
     * @param  size the number of elements in the array
     */
      public ArrayIterator(T[] elem, int size) {
         elements = elem;
         count = size;
         current = 0;
      }


      public boolean hasNext() {
         return current < count;
      }


      public T next() {
         if(!hasNext()) {
            throw new NoSuchElementException();
         }

         Random r = new Random();
         int rand = r.nextInt(size);


         if (prevRand == rand) {
            rand = r.nextInt(size);
         }

         prevRand = rand;

         current++;
         return elements[rand];
      }

    //unsupported operation
      public void remove() {
         throw new UnsupportedOperationException();
      }
   }
}
