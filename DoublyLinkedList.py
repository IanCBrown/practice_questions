import gc

# doubly linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        """print list"""
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def get_size(self):
        """return size of list"""
        return self.length
    
    def insert_head(self, data):
        new_node = Node(data)
        # list is empty 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head = new_node
        self.length += 1
        
    def insert_tail(self, data):
        new_node = Node(data)
        # list is empty 
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insert_after(self, ref_node, data):
        """TODO"""
        return

    def insert_before(self, ref_node, data):
        """TODO"""
        return

    def remove(self, node):
        # node = Node(data)
        """ remove specified element """
        if self.head is None or node is None:
            return 
        
        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None: 
            node.prev.next = node.next
        self.length -= 1
        # garbage collection
        gc.collect()


def main():
    dll = DoublyLinkedList()
    dll.insert_head(1)
    dll.insert_head(2)
    dll.insert_head(3)
    dll.print_list()
    print(dll.get_size())

    dll.insert_tail(5)
    dll.print_list()
    dll.remove(dll.head.next)
    dll.print_list()

if __name__ == '__main__':
    main()
    

            
        
        

