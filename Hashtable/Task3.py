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
        if self.load > (2 / 3):  # Implementing dynamic hashing
            self.dynamic_hashing()

        position = self.hash(key)  # Gets the hash value for the key

        step = 1  # A value to implement quadratic probing
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
                position = (position + step) % self.table_size  # If table[position] is taken by other key,
                step = (step + 1) ** 2  # Quadratic probing
                self.probe_count += 1  # Increment the probe count
                if i == 0:  # if the hash value collided, (i == 0, to prevent incrementing multiple times)
                    self.collision_count += 1

    def __getitem__(self, key):
        """
        Overriding array[index]
        :param key: Key to search
        :return: Value for the key
        :precondition: hash() must have no error
        :complexity: Best Case : O(1), Worst Case O(N)
        """
        position = self.hash(key)  # Gets the hash value

        step = 1
        for _ in range(self.table_size):
            if self.array[position] is None:  # If there's no item at the hash value or next hash values for the key, meaning key does not exist in the table
                raise KeyError("Key does not exist")
            elif self.array[position][0] == key:  # if key found,
                return self.array[position][1]  # return the value for the key
            else:
                position = (position + step) % self.table_size  # Continue to next position
                step = (step + 1) ** 2  # Quadratic probing
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

        step = 1
        for _ in range(self.table_size):  # Below codes are the same as __getitem__
            if self.array[position] is None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (position + step) % self.table_size  # Continue to next position
                step = (step + 1) ** 2  # Quadratic probing
        return False

    def dynamic_hashing(self):
        """
        Makes a hash table to be dynamic, to reduce the load
        """
        all_items = referential_array.build_array(self.count)  # Stores all keys in the hash table before changing the self.array
        j = 0
        for i in range(len(self.array)):
            if self.array[i] is not None:
                all_items[j] = self.array[i]  # Copies the key and value
                j += 1

        self.table_size = (self.table_size * 2) + 1  # Doubles the size and + 1 to make it to odd number
        self.array = referential_array.build_array(self.table_size)  # Making the table bigger
        self.load = round(self.count / self.table_size, 3)  # Updates the load after resizing the table

        self.collision_count = 0  # Resets all the counts before rehashing the items
        self.probe_count = 0
        self.count = 0
        for i in range(len(all_items)):
            self[all_items[i][0]] = all_items[i][1]  # Rehash the items
