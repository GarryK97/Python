from LinkedList import LinkedList
import referential_array


class HashTable:

    def __init__(self, size, a_mult):
        """
        Initializes an object's variables
        :param size: table size (array size) of hash table
        :param a_mult: Multiplier value for hash() function
        :complexity: O(N)
        """
        self.table = referential_array.build_array(size)
        for i in range(size):  # Making table into LinkedList (Separate Chaining)
            a_linkedlist = LinkedList()  # Making a LinkedList object
            self.table[i] = a_linkedlist

        self.count = 0  # Stores the number of items
        self.table_size = size  # Stores the maximum size
        self.mult = a_mult

        self.load = 0  # Stores the load
        self.collision_count = 0  # Stores the number of collisions
        self.probe_count = 0  # Stores the number of probing to find an empty place
        self.avg_probe_len = 0  # Stores the average probe length

    def hash(self, key):
        """
        Calculates the hash value for the given key
        :param key: Key to hash
        :return: Calculated hash value
        :complexity: O(N)
        """
        assert isinstance(key, str), "Key must be string type"  # Handling invalid input as the code only works for string key
        prime_mult = self.mult  # A multiplier to make the hash values unique
        result = 0
        for character in key:  # for each character,
            result = (result * prime_mult + ord(character)) % self.table_size  # % self.table_size will prevent going beyond the limit
        return result

    def __setitem__(self, key, value):
        """
        Overriding array[index] = item, python built-in
        :param key: Key to add or set to the hash table
        :param value: Value that matches the key
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        hash_value = self.hash(key)  # Gets the hash value for the key
        list_atposition = self.table[hash_value]  # list_atposition = Linked List at the hash value of the key

        for i in range(len(list_atposition)):
            if list_atposition[i][0] == key:  # If the key exists in hash table,
                list_atposition[i] = (key, value)  # Replace the key to the new value
                self.avg_probe_len = round(self.probe_count / self.count, 3)  # Updates after probe count change
                return
            else:
                self.probe_count += 1  # probe count += 1 in every i iteration (search)
                if i == 0:  # if the hash value collided, (i == 0, to prevent incrementing multiple times)
                    self.collision_count += 1

        list_atposition.append((key, value))  # If the key is not found(= New key), add a new hash item
        self.count += 1
        self.avg_probe_len = round(self.probe_count / self.count, 3)  # Updates after adding an item
        self.load = round(self.count / self.table_size, 3)  # Updates the load after adding an item

    def __getitem__(self, key):
        """
        Overriding array[index]
        :param key: Key to search
        :return: Value for the key
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        hash_value = self.hash(key)  # Gets the hash value for the key
        list_atposition = self.table[hash_value]  # list_atposition = Linked List at the hash value of the key

        for i in range(len(list_atposition)):
            if list_atposition[i][0] == key:  # if the key found,
                return list_atposition[i][1]  # return the value for the key
        raise KeyError("Key does not exist")  # Meaning : Searched all elements but key not found

    def __contains__(self, key):
        """
        Overriding foo in array, returns true if the given key is in the hash table. Else, false
        :param key: Key to search
        :return: Boolean, whether key exists in the table or not
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        hash_value = self.hash(key)  # Gets the hash value for the key
        list_atposition = self.table[hash_value]  # list_atposition = Linked List at the hash value of the key

        for i in range(len(list_atposition)):  # Below codes are the same as __getitem__
            if list_atposition[i][0] == key:
                return True
        return False
