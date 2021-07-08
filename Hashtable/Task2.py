import referential_array


class HashTable:

    def __init__(self, size, a_mult):
        """
        Initializes an object's variables
        :param size: table size (array size) of hash table
        :param a_mult: Multiplier value for hash() function
        :complexity: O(1)
        """
        self.array = referential_array.build_array(size)
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
        position = self.hash(key)  # Gets the hash value for the key

        for i in range(self.table_size):
            if self.array[position] is None:  # If table[position] is empty,
                self.array[position] = (key, value)  # Set the table[position] to new key and value
                self.count += 1  # Increment the count to store the number of items
                self.load = round(self.count / self.table_size, 3)  # Updates the load after adding an item
                self.avg_probe_len = round(self.probe_count / self.count, 3)  # Updates average probe length
                return  # to end the function
            elif self.array[position][0] == key:  # Meaning : the user wants to change the value for an existing key
                self.array[position] = (key, value)
                self.avg_probe_len = round(self.probe_count / self.count, 3)  # Updates average probe length
                return
            else:
                position = (position + 1) % self.table_size  # If table[position] is taken by other key, probe to next position (Linear Probing)
                self.probe_count += 1  # Increment the probe count
                if i == 0:  # if the hash value collided, (i == 0, to prevent incrementing multiple times)
                    self.collision_count += 1

        raise Exception("Hash table is full and Key does not exist")  # Meaning : Hash table is full and the given key does not exist

    def __getitem__(self, key):
        """
        Overriding array[index]
        :param key: Key to search
        :return: Value for the key
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        position = self.hash(key)  # Gets the hash value

        for _ in range(self.table_size):
            if self.array[position] is None:  # If there's no item at the hash value or next hash values for the key, meaning key does not exist in the table
                raise KeyError("Key does not exist")
            elif self.array[position][0] == key:  # if key found,
                return self.array[position][1]  # return the value for the key
            else:
                position = (position + 1) % self.table_size  # Continue to next position
        raise KeyError("Key does not exist")  # Meaning : Searched all elements but key not found

    def __contains__(self, key):
        """
        Overriding foo in array, returns true if the given key is in the hash table. Else, false
        :param key: Key to search
        :return: Boolean, whether key exists in the table or not
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        position = self.hash(key)  # Gets the hash value

        for _ in range(self.table_size):  # Below codes are the same as __getitem__
            if self.array[position] is None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (position + 1) % self.table_size  # Continue to next position
        return False
