"""
This project is creating a Linked List using the Python
programming language.
"""

# Node Class
class Node:
    # Init function
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Linked List class:
class LinkedList:
    # Init function
    def __init__(self):
        self.head = None
    
    # This function prints linked list
    def print_list(self):
        # Create a temp node and set it to the head
        temp = self.head

        # Loop through linked list
        # This loop ends when it finds an null node
        while (temp):
            # Print the data
            print(temp.data)
            #Iterate to next node
            temp = temp.next

    # This function inserts at the front of the linked list
    def insert_at_front(self, new_data):
        # Create the new node
        new_node = Node(new_data)
        # Set the new node's next node to the current head
        new_node.next = self.head
        # Move the head to point to the new node
        self.head = new_node

    def insert_at_given_point(self, new_data, prev_node):
        # First, check if the given previous node exists
        if prev_node is None:
            print("The given node must exist in the current linked list")
            return
        
        # Create the node the data
        new_node = Node(new_data)
        # Make the next of new node as next of prev_node
        new_node.next = prev_node.next
        # Make next of prev_node as new_node
        prev_node.next = new_node

    def insert_at_end(self, new_data):
        # Create the new node
        new_node = Node(new_data)
        # Check if list is empty
        # If it is empty, new Node is the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse until the last node
        last = self.head
        while (last.next):
            last = last.next

        # Change the next of last to the new node
        last.next = new_node

# Main 

if __name__ == '__main__':

    # Create an empty list
    linked_list = LinkedList()

    # Create a head and nodes
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Set head.next to second and second.next to third
    linked_list.head.next = second
    second.next = third

    linked_list.insert_at_front(10)
    linked_list.insert_at_given_point(55, second)
    linked_list.insert_at_end(23)

    # Call print_list() function
    linked_list.print_list()