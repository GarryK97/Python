from referential_array import build_array


class ListIterator:
    """
    Iterator class for List(array) objects
    """
    def __init__(self, array, length):
        """
        :param array: any list(array) to iter
        :param length: length of the array
        :complexity: O(1)
        """
        self.current = 0    # Default Starting index (fixed to 0, in normal use)
        self.array = array
        self.size = length

    def __iter__(self):  # called by iter(foo)
        """
        Make a class iterable
        :return: the object itself
        :complexity: O(1)
        """
        return self  # To make a class iterable (Initializing), otherwise will cause error.

    def __next__(self):  # called by next(foo)
        """
        Using self.current(index), returns list item at index and increments the self.current to go to next index
        :return: list[self.current]
        :precondition: __getitem__ must have no error
        :complexity: O(1)
        """
        if self.current >= self.size:  # if self.current(index) exceeded the size of the list
            raise StopIteration                                             # OR if current item is None, StopIteration
        else:
            item_toreturn = self.array[self.current]  # Saving the item before incrementing self.current
            self.current += 1  # Increment self.current to go to next index
            return item_toreturn


class Array_Based_List:
    """
    User-defined array class (fixed size list)
    """
    def __init__(self):
        """
        Initializing variables for the class object
        :complexity: O(1)
        """
        self.array = build_array(20)  # Make an array, using imported library, build_array(20) (Task2 Rule)
        self.count = 0  # counts the number of elements of the array. (Simply, the real length of the array)
        self.size = 20  # Saves the total size of the array

    def __str__(self):  # Called by str(foo)
        """
        Makes an array into string representation, one element per line (Assignment2 Rule)
        :return: the string representation of the array
        :precondtion: __len__, __getitem__ must have no error
        :complexity: O(N)
        """
        string = ""  # Initializing temporary string
        for i in range(len(self)):
            string += str(self[i]) + "\n"  # e.g.) string = "1\n2\n3\n", \n = new line, so one element per line.
        return string

    def __len__(self):  # Called by len(foo)
        """
        Returns the real length of the array, by using self.count
        :return: self.count (length of the array)
        :complexity: O(1)
        """
        return self.count

    def __contains__(self, item): # Called by foo in self
        """
        Finds the item in the list
        :param item: query item to search
        :return: True, if found. False, if not found.
        :precondition: __len__, __getitem__ must have no error
        :complexity: O(N)
        """
        for i in range(len(self)):
            if self[i] == item:
                return True  # if any element equals item, return True
        return False    # if no element equals item, return False

    def is_index_inbound(self, index):
        """
        Checks whether the index is in boundary of the list (Also, checks whether the list is empty or not)
        :param index: index to check (int type)
        :return: True, if index is in boundary. False, if out of boundary.
        :precondition: __len__ must have no error
        :complexity: O(1)
        """
        assert isinstance(index, int), "index argument must be int type"
        if index >= 0:  # if index is positive number,
            return index < len(self)  # positive index must be less than positive length of the list
        if index < 0:   # if index is negative number,
            return index >= -len(self)  # negative index must be greater or equal to negative length of the list

    def __getitem__(self, index):  # Called by self[index]
        """
        Gets the item at the index
        :param index: index of the list (int type)
        :return: the list item at the index
        :precondition: is_index_inbound() must have no error
        :complexity: O(1)
        """
        if not self.is_index_inbound(index):  # if the index is out of boundary,
            raise IndexError("The index is Out of Boundary")  # raise Error
        elif index >= 0:  # if positive index,
            return self.array[index]
        else:  # if negative index,
            return self.array[index % self.count]  # Using a math rule. (e.g. -1 % 5 = 4, so -1 will give last element)

    def __setitem__(self, index, item):  # Called by self[index] = foo
        """
        Changes(sets) the list element at index to new item
        :param index: index, to set the item (int type)
        :param item: item to set it at the index
        :precondtion: is_index_inbound() must have no error
        :complexity: O(1)
        """
        if not self.is_index_inbound(index):  # Checking whether the index input is in boundary
            raise IndexError("The Index is Out of Boundary")
        elif index >= 0:  # if positive index,
            self.array[index] = item
        else:  # if negative index,
            self.array[index % self.count] = item   # Same as __getitem__

    def __eq__(self, other):  # Called by foo == bar
        """
        Checks whether self is equivalent to the list 'other' or not
        The max size of array is not considered, as it uses self.count, which is (__len__).
        :param other: list to check
        :return: True, if two lists equivalent. False, if not.
        :precondition: __len__, __getitem__ must have no error
        :complexity: Best Case : O(1), Worst Case : O(N)
        """
        if len(self) != len(other):
            return False  # if the length is different, immediately return False
        else:   # if the lengths are the same,
            for i in range(len(self)):  # Only one for loop required as they have the same length
                if self[i] != other[i]:
                    return False  # if any element is different from other list's element, return False
            return True  # if all checked, return True

    def is_full(self):
        """
        Checks whether the array is full or not
        :return: True, if full. False, if not full
        :precondition: __len__ must have no error
        :complexity: O(1)
        """
        return len(self) >= self.size  # return self.count > max size of the array

    def append(self, item):
        """
        Adds the item at the end of the list (next to the last element)
        :param item: item to add
        :precondition: is_full(), __setitem__, make_dynamic() must have no error
        :complexity: Best Case : O(1), Worst Case : O(N) , including make_dynamic()
        """
        self.make_dynamic()  # Checks whether the array is full or not, if full, enlarges the array size
        self.array[self.count] = item  # because self.count always point to the last index + 1
        self.count += 1  # to update the length

    def insert(self, index, item):
        """
        Inserts the item into list at the index.
        :param index: index to put the item (int type)
        :param item: item to be inserted
        :precondition: is_full(), is_index_inbound(), __len__, __setitem__, __getitem__, make_dynamic() must have no error
        :complexity: O(N) , including make_dynamic()
        """
        assert isinstance(index, int), "insert(index, item): index must be int type"  # Checks if the index is int type
        if index == len(self):  # If user wants to insert the item after last element,
            self.array[index] = item  # Same as append function
            self.count += 1
        elif not self.is_index_inbound(index):
            raise IndexError("The index is Out of Boundary")  # if the index is out of boundary, raise error
        else:
            self.make_dynamic()  # To checks if the array is full and enlarges it if necessary
            if index < 0:
                index = index % len(self)  # # to prevent negative index messes up for loop
            for i in range(len(self)-1, index-1, -1):
                self.array[i+1] = self.array[i]  # push the items behind from index to end, to make a space
            self[index] = item  # put the argument 'item' into the index
            self.count += 1  # to update the length

    def remove(self, item):
        """
        Removes the first instance of the item from the list
        :param item: item to remove
        :precondition: __len__, __getitem__, __setitem__, make_dynamic() must have no error
        :complexity: O(N^2) , including make_dynamic
        """
        for i in range(len(self)):
            if self[i] == item:  # Searches the list item that equals the query item
                for j in range(i, len(self)-1):
                    self[j] = self[j+1]  # if found, push the elements behind index in front
                self.count -= 1  # Update the length      # the index item will be automatically removed
                self.make_dynamic()  # To check available space, to make the array dynamic after removing the item
                return
        raise ValueError("The item does not exist in the list")  # if not found, raise Error

    def delete(self, index):
        """
        Removes the list item at the index
        :param index: index to be deleted (int type)
        :precondtion: is_index_inbound(), __len__, __getitem__, __setitem__, make_dynamic() must have no errors
        :complexity: O(N) , including make_dynamic()
        """
        assert isinstance(index, int), "delete(index) : index must be int type"  # Checks if item is int
        if not self.is_index_inbound(index):
            raise IndexError("The index is Out of Boundary")  # if the index is not in boundary, raise Error
        else:
            if index < 0:
                index = index % len(self)  # to prevent negative index messes up for loop
            for i in range(index, len(self)-1):
                self[i] = self[i+1]  # same as remove() function, pushing elements in front
            self.count -= 1  # Update the length
            self.make_dynamic()  # To make the array dynamic after deleting the item (checking unnecessary space)

    def sort(self, reverse):
        """
        Sorts the list, using insertion sort algorithm. if reverse == True, sorts the list in descending order
        :param reverse: (bool type) False = ascending order, True = descending order
        :precondition: 1. the list must have all elements the same type. (Otherwise, will cause TypeError)
                       2. __len__, __getitem__, __setitem__ must have no errors
        :complexity: Best Case : O(N), Worst Case : O(N^2)
        """
        assert isinstance(reverse, bool), "reverse argument must be boolean type."  # Checks if reverse is bool type
        assert len(self) > 0, "The list must have at least one item"  # Checks if the list can be sorted
        ### Insertion Sort Algorithm ###
        for i in range(1, len(self)):
            current_item = self[i]  # Save current_item for later use
            j = i-1  # To compare front elements from current_item
            if not reverse:
                while j >= 0 and current_item < self[j]: # j >= 0, to prevent error
                    self[j+1] = self[j] # Move elements to next index to insert current_item in front
                    j -= 1  # j -= 1, to compare the next front item (j can be -1, but can handle later)
            else:   # Reverse
                while j >= 0 and current_item > self[j]:
                    self[j+1] = self[j]
                    j -= 1
            self[j+1] = current_item  # if all checked, insert the item into appropriate index
                                            # Even j = -1, item will be inserted at 0 due to [j+1]

    def __iter__(self):  # Called by iter(foo), used by for loop
        """
        Making this class iterable, by using ListIterator class defined above.
        :return: initialized iterator
        :precondition: ListIterator class must have no error
        :complexity: O(1)
        """
        return ListIterator(self.array, self.count)

    def copy(self):
        """
        Makes a copy of a list and returns it
        :return: Copy of self list
        :precondition: __len__, __getitem__, append() must have no errors
        :complexity: O(N)
        """
        copylist = Array_Based_List()
        for i in range(len(self)):
            copylist.append(self.array[i])
        return copylist

    def make_dynamic(self):
        """
        Checks the list and changes the size of the list if necessary
        :precondition: is.full(), __iter__, append() must have no error
        :complexity: Best Case : O(1), Worst Case : O(N)
        """
        if self.is_full():  # If full, the array needs to be resized larger
            new_array = build_array(self.size * 2)  # Original size * 2
            for i in range(len(self)):
                new_array[i] = self[i]  # Copying the original item to new array
            self.array = new_array  # Replace self.array to enlarged array
            self.size = self.size * 2  # Update the total size of the array
        else:
            available_space = self.size - self.count
            if self.size > 20 and self.count < (available_space // 8):
                # If size bigger than base size(20), and the occupied space less than (1/8 * available space)
                new_array = build_array(self.size // 2)  # Same process with the above code
                for i in range(len(self)):
                    new_array[i] = self[i]
                self.array = new_array
                self.size = self.size // 2