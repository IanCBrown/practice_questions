import java.util.Iterator;
import java.util.NoSuchElementException;

// use nodes!!
public class LinkedList<T> implements DoubleEndedList<T> {

   private Node front;
   private Node rear;
   private int size;


   public LinkedList() {
      front = null;
      size = 0;
   }

    //addFirst
   public void addFirst(T element) {
      if (element == null) {
         throw new IllegalArgumentException();
      }

      Node n = new Node(element);

      if (isEmpty()) {
         rear = n;
         front = n;
      }

      front.prev = n;
      n.next = front;
      front = n;
      size++;
   }

    //addLast
   public void addLast(T element) {
      if (element == null) {
         throw new IllegalArgumentException();
      }

      Node n = new Node(element);

      if (isEmpty()) {
         rear = n;
         front = n;
      }


      rear.next = n;
      n.prev = rear;
      rear = n;
      size++;
   }

    //removeFirst
   public T removeFirst() {
      if (isEmpty()) {
         return null;
      }

      Node n = front;

      if (size == 1) {
         front = null;
         size--;
      }
      else {

         front = front.next;
         front.prev = null;
         size--;
      }
      return n.element;
   }

    //removeLast
   public T removeLast() {
      if (isEmpty()) {
         return null;
      }

      Node n = rear;

      if (size == 1) {
        front = null;
        size--;
      }
      else {
        rear = rear.prev;
        rear.next = null;
        size--;
      }
      return n.element;
   }

    //size - from List interface
   public int size() {
      return size;
   }

    //isEmpty - from LIst Interface
   public boolean isEmpty() {
      return front == null;
   }

    //iterator???????? -- from list
   @Override
    public Iterator<T> iterator() {
      return new LinkedIterator();
   }




////////////////////
// Nested classes //
////////////////////


// private class Node {}
/** Defines node */
   private class Node {
      private T element;
      private Node next;
      private Node prev;

      public Node(T e) {
         element = e;
      }
   }


// private class iterator {}
   private class LinkedIterator implements Iterator<T> {

      private Node current = front;

    //hasNext
      public boolean hasNext() {
         return current != null;
      }

    //next
      public T next() {
         if (!(hasNext())) {
            throw new NoSuchElementException();
         }

         T result = current.element;
         current = current.next;
         return result;
      }

    //remove
      public void remove() {
         throw new UnsupportedOperationException();
      }

   }
}
