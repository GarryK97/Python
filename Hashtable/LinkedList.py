class LinkedListIterator:
    """
    Iterator class for List(array) objects
    """

    def __init__(self, head):
        """
        Initializing class object's variable
        :param head: head of the linked list (start node)
        """
        self.current = head

    def __iter__(self):  # called by iter(foo)
        """
        Making a class iterable
        :return: the object itself
        :complexity: O(1)
        """
        return self  # To make a class iterable (Initializing), otherwise will cause error.

    def __next__(self):  # called by next(foo)
        """
        When called, returns the item and updates self.current to next node
        :return: self.current.item
        :precondition: self.current (head) should be object of Node class
        :complexity: O(1)
        """
        if self.current is None:  # means linked list reached the end, so need to stop
            raise StopIteration
        else:
            item_toreturn = self.current.item  # Saving the item before updating self.current to next node
            self.current = self.current.next  # Updates the self.current to next node
            return item_toreturn  # Returns the saved item


class Node:
    """
    Basic and fundamental class to make a linked list
    """

    def __init__(self, item, next):
        """
        Initializing class object variables
        :param item: item to be added
        :param next: Next node (to link current node to next node)
        """
        self.item = item
        self.next = next


class LinkedList:
    """
    Linked list class
    """

    def __init__(self):
        """
        Initializing class object variables
        """
        self.head = None  # set head to None, means no element yet
        self.count = 0  # saves the length of the list

    def __str__(self):  # Called by str(foo)
        """
        Returns the string representation of the list
        :return: String representation of list
        :precondition: __len__ must have no error
        :complexity: O(N)
        """
        string = ""
        node = self.head  # Gets the start node
        for i in range(len(self)):  # Loop through all elements
            string += str(node.item) + "\n"  # \n = new line, so one item per line
            node = node.next  # Continue to next node
        return string  # Returns the string representation

    def __len__(self):  # Called by len(foo)
        """
        Returns the length of the list
        :return: self.count (length)
        :complexity: O(1)
        """
        return self.count  # Simply, returns the length of the list

    def is_empty(self):
        """
        Checks whether the list is empty or not
        :return: True, if empty. False, if not empty
        :complexity: O(1)
        """
        return self.head is None  # self.head = None means there is no start node, which means empty

    def __contains__(self, item):  # Called by, foo in bar
        """
        Checks if the query item exists in the list
        :param item: query item to search
        :return: True, if found. False, if not Found
        :precondition: __len__ must have no error
        :complexity: O(N)
        """
        node = self.head
        for i in range(len(self)):  # Loop through all item
            if node.item == item:  # if any element == item,
                return True
            node = node.next  # Continue to next node
        return False  # If not found, return False

    def is_inbound(self, index):
        """
        Checks if the index is in range of the list
        :param index: index to check
        :return: True, if index is in range. False, if not.
        :precondition: __len__ must have no error
        :complexity: O(1)
        """
        if index >= 0:
            return index < len(self)  # e.g.) [1,2,3], index of 3 is not 3, so exclusive
        elif index < 0:
            return index >= -len(self)  # e.g.) [1,2,3], index of 1 is -3, so inclusive

    def __getitem__(self, index):  # Called by, foo[index]
        """
        Gets the item at the index
        :param index: index position to get item
        :return: item at the index
        :precondition: is_inbound(), __len__ must have no error
        :complexity: O(N)
        """
        if not self.is_inbound(index):  # Checking validity of index
            raise IndexError("Index is out of boundary")
        elif index >= 0:  # If index is non-negative,
            node = self.head
            for i in range(index):  # Loop until it reaches the index
                node = node.next
            return node.item  # Return the index item
        else:  # If index is negative,
            node = self.head
            index = index % len(self)  # Using a math rule, -1 % 5 = 4, so -1 will refer to the last element
            for i in range(index):  # Same process
                node = node.next
            return node.item

    def get_node(self, index):
        """
        Gets the node at the index
        :param index: index position to get node
        :return: node at the index
        :precondition: is_inbound(), __len__ must have no error
        :complexity: O(N)
        """
        if not self.is_inbound(index):  # Checking index
            raise IndexError("Index is out of boundary")
        elif index >= 0:  # Same process with __getitem__, only difference is get_node() returns the node, not item
            node = self.head
            for i in range(index):
                node = node.next
            return node
        else:
            node = self.head
            index = index % len(self)
            for i in range(index):
                node = node.next
            return node

    def __setitem__(self, index, item):  # Called by, foo[index] = bar
        """
        Sets the existing index item to input item
        :param index: index position to set
        :param item: item to set
        :precondition: is_inbound(), __len__ must have no error
        :complexity: O(N)
        """
        if not self.is_inbound(index):  # Checking index
            raise IndexError("Index is out of boundary")
        elif index >= 0:  # If index non-negative,
            node = self.head
            for i in range(index):
                node = node.next
        else:  # if index negative,
            node = self.head
            index = index % len(self)
            for i in range(index):
                node = node.next
        node.item = item  # Sets the index item to input item

    def __eq__(self, other):
        """
        Checks whether self is the same list as other
        :param other: Another list to check
        :return: True, if equal. False, if not equal.
        :precondition: __len__, __getitem__ must have no error
        :complexity: Best Case : O(1), Worst Case : O(N)
        """
        if len(self) != len(other):  # if length is different, return False immediately
            return False
        for i in range(len(self)):  # Check all elements
            if self[i] != other[i]:  # If any element is different from other's element
                return False
        return True

    def append(self, item):
        """
        Adds the item after the last item
        :param item: item to add
        :precondition: is_empty(), get_node() must have no error
        :complexity: O(N), including get_node()
        """
        if self.is_empty():  # if the list is empty, it means no next node
            self.head = Node(item, None)  # sets self.head(start node) to new node immediately
        else:
            new_node = Node(item, None)  # Creates a new node with next node = None, because it will be added to last
            last_node = self.get_node(-1)  # Gets the last node
            last_node.next = new_node  # Changes the last_node.next to new node, to link
        self.count += 1  # Updates the length

    def insert(self, index, item):
        """
        Inserts the input item at index
        :param index: index position to insert
        :param item: item to put
        :precondtion: __len__, append(), is_inbound(), get_node must have no errors
        :complexity: O(N), including get_node()
        """
        if index == len(self):  # if user wants to insert the item at the last,
            self.append(item)  # Use append function (Because both are doing the same task in this case)
        elif not self.is_inbound(index):  # Checking index
            raise IndexError("Index is out of boundary")
        elif index == 0 or index == -len(
                self):  # if index = 0, it needs to be treated differently to prevent error, e.g.) self.get_node(0-1) will give the last node
            self.head = Node(item,
                             self.head)  # Sets start node to new node and links the new node to original start node.
            self.count += 1  # Updates the length
        else:
            original_node = self.get_node(index - 1)  # Gets previous node (original node)
            new_node = Node(item, original_node.next)  # Similar process with the above
            original_node.next = new_node
            self.count += 1

    def remove(self, item):
        """
        Removes the first instance of input item in the list
        :param item: item to remove
        :precondition: __len__, __getitem__, get_node() must have no errors
        :complexity: Best Case : O(N), Average Case : O(N^2), including get_node()
        """
        for index in range(len(self)):  # Loop through all index
            if self[index] == item:  # if item found,
                if index == 0:  # if index of the item found is 0,
                    self.head = self.head.next  # Changes start node to next node (automatically item will be removed)
                else:
                    node_todelete = self.get_node(index)  # Gets the node at index of the item
                    previous_node = self.get_node(index - 1)  # Gets the previous node
                    previous_node.next = node_todelete.next  # Similar process (Cuts the link to the item node)
                self.count -= 1  # Updates the length
                return
        raise ValueError("The item does not exist in the list")  # If item not found, raise error

    def delete(self, index):
        """
        Deletes the item at index
        :param index: index to delete
        :precondition: is_empty(), is_inbound, get_node() must have no error
        :complexity: O(N), including get_node()
        """
        if self.is_empty():  # If empty, it means nothing to delete
            raise IndexError("The list is empty")
        elif not self.is_inbound(index):  # Checking index
            raise IndexError("Index is out of boundary")
        elif index == 0 or index == -len(self):  # Same mechanism with remove()
            self.head = self.head.next  # Cuts the link to the index node
        else:
            node_todelete = self.get_node(index)  # Same mechanism with remove()
            previous_node = self.get_node(index - 1)
            previous_node.next = node_todelete.next
        self.count -= 1

    def sort(self, reverse):
        """
        Sorts the list based on reverse value, using insertion sorting algorithm
        There is no need to change node.next because length remains the same and items should be linked as well.
        :param reverse: bool type. if True, sorting in ascending order. False, sorting in descending order.
        :precondition: __len__, get_node(), __getitem__, __setitem__ must have no error
        :complexity: Best Case : O(N), Average(Worst) Case : O(N^2)
        """
        assert len(self) > 0, "The list must have at least one item"  # Checks if the list can be sorted
        ### Insertion Sort ###
        for i in range(1, len(self)):
            current_item = self[i]  # Saves the current item that is checked
            j = i - 1  # j < i (j will be always be previous index of index i)
            if not reverse:
                while j >= 0 and self[j] > current_item:  # j >= 0, to prevent error. While previous item > current_item
                    self[j + 1] = self[j]  # Push elements behind to make space for current_item
                    j -= 1  # Continue to next previous index (before previous index)
            else:
                while j >= 0 and self[j] < current_item:  # Similar process, but reversed
                    self[j + 1] = self[j]
                    j -= 1
            self[j + 1] = current_item  # Put the current_item at appropriate position

    def __iter__(self):
        """
        Making this class iterable
        :return: Iterator (required for iteration)
        :precondition: LinkedListIterator class has no error
        :complexity: O(1)
        """
        return LinkedListIterator(self.head)
