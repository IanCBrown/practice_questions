# singly linked list implementation

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 
        

class LinkedList: 
    def __init__(self): 
        self.head = None

    def print_list(self): 
        """ print list """
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def insert_front(self, data):
        """ insert new node into front of list """ 
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node 

    def insert_tail(self, data):
        """ insert new node into front of end of list """ 
        new_node = Node(data)
        temp = self.head
        while (temp):
            if temp.next == None:
                temp.next = new_node
                new_node.next = None
                return
            temp = temp.next

    def remove_first(self):
        """ remove first item from linked list"""
        temp = self.head
        self.head = temp.next
        temp = None

    def remove_last(self):
        """ remove last item from list """
        temp = self.head
        while (temp):
            if temp.next == None:
                temp = None
                return 
            temp = temp.next




# Execution starts here
if __name__ =='__main__':
    llist = LinkedList() 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3) 

    llist.head.next = second
    second.next = third
    # list state: 1 2 3 
    llist.print_list()

    # list state: 2 3
    llist.remove_first()
    llist.print_list()

    # list state: 10 2 3
    llist.insert_front(10)
    llist.print_list()

    # list state: 10 2 3 11
    llist.insert_tail(11)
    llist.print_list()

