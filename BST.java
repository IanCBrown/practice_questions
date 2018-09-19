
public class BST {

    public static Node root; 

    public static void main(String[] args) {
        BST b = new BST(); 
        b.insert(3);b.insert(8);
		b.insert(1);b.insert(4);b.insert(6);b.insert(2);b.insert(10);b.insert(9);
		b.insert(20);b.insert(25);b.insert(15);b.insert(16);
        b.display(b.root);  
    }

    public boolean find(int n) {
        Node current = root;  
        while (current != null) {
            if (current.data == n) {
                return true; 
            }
            else if (current.data > n) {
                current = current.left;
            }
            else {
                current = current.right; 
            }
        }
        return false; 
    }

    public void insert(int n) {
        Node newNode = new Node(n); 
        if (root == null) {
            root = newNode; 
            return; 
        }
        Node current = root; 
        Node parent = null; 
        while (true) {
            parent = current; 
            if (current.data > n) {
                current = current.left; 
                if (current == null) {
                    parent.left = newNode; 
                    return;  
                }
            } else {
                current = current.right; 
                if (current == null) {
                    parent.right = newNode; 
                    return; 
                }
            }
        }
    }   

    public void display(Node root) {
        if (root != null) {
            display(root.left); 
            System.out.print(" " + root.data); 
            display(root.right); 
        }
    }

    class Node {
        int data; 
        Node left; 
        Node right; 
    
        public Node(int data) {
            this.data = data; 
            left = null; 
            right = null; 
        }
    }
}

