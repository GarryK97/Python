from Task4 import HashTable


def hash_test():
    # As hash() function simply calculates the hash value, I focused on whether the hash() is within the range and
    # can detect errors or not

    a_table = HashTable(1, 1)

    try:  # Checks if hash() can detect invalid integer inputs
        a_table.hash(123)
        a_table.hash(1)
        a_table.hash(3597)
    except AssertionError:  # Ignore AssertionError because it means the function is working as expected
        pass

    a_table.hash("John")  # Below codes should not cause any error
    a_table.hash("1378")
    a_table.hash("Error?")
    a_table.hash("ASDIwhdaisdiahi12sdijawi123Error?")


def __setitem__test():
    # Used lecture examples for testing (because it's very time consuming to calculate all the hash values)
    value = "Test"  # Temporary placeholder value for testing
    test_keys = ["Aho", "Kruse", "Standish", "Horowitz", "Langsam", "Sedgewick", "Knuth"]  # Testing Keys

    a_table = HashTable(101, 31)
    for key in test_keys:
        a_table[key] = value  # Calling __setitem__ function

    # Checking if keys are mapped to correct table position (Hash value) and checks if the function correctly probe for an empty space
    assert a_table.table[49][0][0] == "Aho" and a_table.table[95][0][0] == "Kruse" and a_table.table[60][0][0] == "Standish", "__setitem__ : Not working as expected"
    assert a_table.table[28][0][0] == "Horowitz" and a_table.table[21][0][0] == "Langsam" and a_table.table[24][0][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert a_table.table[44][0][0] == "Knuth", "__setitem__ : Not working as expected"

    # Below codes are the same as above
    b_table = HashTable(128, 1024)
    for key in test_keys:
        b_table[key] = value

    assert b_table.table[111][0][0] == "Aho" and b_table.table[101][0][0] == "Kruse" and b_table.table[104][0][0] == "Standish", "__setitem__ : Not working as expected"
    assert b_table.table[122][0][0] == "Horowitz" and b_table.table[109][0][0] == "Langsam" and b_table.table[107][0][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert b_table.table[104][1][0] == "Knuth", "__setitem__ : Not working as expected"

    c_table = HashTable(7, 3)
    for key in test_keys:
        c_table[key] = value

    assert c_table.table[0][0][0] == "Aho" and c_table.table[5][0][0] == "Kruse" and c_table.table[1][0][0] == "Standish", "__setitem__ : Not working as expected"
    assert c_table.table[5][1][0] == "Horowitz" and c_table.table[2][0][0] == "Langsam" and c_table.table[2][1][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert c_table.table[1][1][0] == "Knuth", "__setitem__ : Not working as expected"


def __getitem__test():
    # Reused the code from __setitem__ and modified for __getitem__ test
    test_keys = ["Aho", "Kruse", "Standish", "Horowitz", "Langsam", "Sedgewick", "Knuth"]

    a_table = HashTable(101, 31)
    for key in test_keys:
        a_table[key] = key  # Inserts test keys to the hash table
    for key in test_keys:
        assert a_table[key] == key, "__getitem__ : Not working as expected"  # Checks if table[key] gives correct value

    # below codes are the same as above
    b_table = HashTable(128, 1024)
    for key in test_keys:
        b_table[key] = key
    for key in test_keys:
        assert b_table[key] == key, "__getitem__ : Not working as expected"

    c_table = HashTable(7, 3)
    for key in test_keys:
        c_table[key] = key
    for key in test_keys:
        assert c_table[key] == key, "__getitem__ : Not working as expected"


def __contains__test():
    value = "Test"
    test_keys = ["Aho", "Kruse", "Standish", "Horowitz", "Langsam", "Sedgewick", "Knuth"]

    a_table = HashTable(101, 31)
    for key in test_keys:
        a_table[key] = value  # Insert test keys into the hash table
    for key in test_keys:
        assert key in a_table, "__contains__ : Not working as expected"  # Checks if __contains__ return correct boolean value
        assert not "Notexisting" in a_table, "__contains__ : Non-existing key returned True"  # This key does not exist, so must return false

    # below codes are the same as above
    b_table = HashTable(128, 1024)
    for key in test_keys:
        b_table[key] = value
    for key in test_keys:
        assert key in b_table, "__contains__ : Not working as expected"
        assert not "Notexisting" in a_table, "__contains__ : Non-existing key returned True"

    c_table = HashTable(7, 3)
    for key in test_keys:
        c_table[key] = value
    for key in test_keys:
        assert key in c_table, "__contains__ : Not working as expected"
        assert not "Notexisting" in a_table, "__contains__ : Non-existing key returned True"

def threefiles_test():
    # Function used to make the prime_mult table for Task2
    ### Testing the 3 files given ###

    # Open files and add them into lists
    f = open("english_small.txt", 'rt', encoding='UTF8')
    eng_small = []
    for line in f:
        line = line.strip()
        eng_small.append(line)
    f.close()

    f = open("english_large.txt", 'rt', encoding='UTF8')
    eng_large = []
    for line in f:
        line = line.strip()
        eng_large.append(line)
    f.close()

    f = open("french.txt", 'rt', encoding='UTF8')
    french = []
    for line in f:
        line = line.strip()
        french.append(line)
    f.close()

    ### Testing Start ###
    value = "test"  # A temporary(placeholder) value for testing
    n = 1
    for text_file in [eng_small, eng_large, french]:
        print("\n---Testing file " + str(n))  # file 1, 2, 3 = eng_small, eng_large, french
        n += 1
        hashtable = HashTable(300151, 1064)  # 300151 and 1064 are the best combinations found in Task2
        for key in text_file:
            hashtable[key] = value

        print("\nMultiplier Value = " + str(1064))
        print("Number of items = " + str(hashtable.count))
        print("Table size = " + str(300151))
        print("Load = " + str(hashtable.load))
        print("Total Collisions = " + str(hashtable.collision_count))
        print("Total Probe Length = " + str(hashtable.probe_count))
        print("Average Probe Length = " + str(hashtable.avg_probe_len))


def Test_Main():
    hash_test()
    __setitem__test()
    __getitem__test()
    __contains__test()
    threefiles_test()


Test_Main()


"""
--- Comparison between Separate Chaining and Linear Probing ---

Collisions:
In all the text files, Separate Chaining had lower collisions than Linear Probing. It is because collision in
Separate Chaining only occurs when the hash value for the keys are the same, however, collision in Linear Probing also 
occurs when the hash value position is already occupied by an other key, although the occupied key has a different
hash value. 
For example, if the keys are [a1, a2, b1, b2, b3, None] (assume a and b, meaning the same hash value) and the system
wants to add c1 which should be inserted at b3, Linear Probing will consider it as a collision, even if the hash value of
two keys are different.

Probe Length:
In all the text files, the probe length of Separate Chaining hash table was very lower than the Linear Probing.
It is because Separate Chaining only searches the elements of the linked list at the hash value position, however,
Linear Probing searches the entire elements until it finds the key or None.
For example, if the keys are [a1, a2, b1, b2, b3, None] (assume a and b, meaning the same hash value) and the system
wants to find a3, Separate Chaining will stop the probing after a2, but Linear Probing will continue to search until it
reaches 'None'. So, in this kind of cases, Separate Chaining will have less probe length than Linear Probing.

Disadvantage of Separate Chaining:
Although Separate Chaining could have less collisions and probe length than Linear probing, it requires more memory than
Linear probing as Separate Chaining must store additional Item.next to make a linked list.

Conclusion:
Separate Chaining is likely to have less collisions and probe length than Linear probing.
However, it requires more memory than Linear probing.
"""