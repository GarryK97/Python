from Task1 import HashTable


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

    # Checking if keys are mapped to correct array position (Hash value) and checks if the function correctly probe for an empty space
    assert a_table.array[49][0] == "Aho" and a_table.array[95][0] == "Kruse" and a_table.array[60][0] == "Standish", "__setitem__ : Not working as expected"
    assert a_table.array[28][0] == "Horowitz" and a_table.array[21][0] == "Langsam" and a_table.array[24][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert a_table.array[44][0] == "Knuth", "__setitem__ : Not working as expected"

    # Below codes are the same as above
    b_table = HashTable(128, 1024)
    for key in test_keys:
        b_table[key] = value

    assert b_table.array[111][0] == "Aho" and b_table.array[101][0] == "Kruse" and b_table.array[104][0] == "Standish", "__setitem__ : Not working as expected"
    assert b_table.array[122][0] == "Horowitz" and b_table.array[109][0] == "Langsam" and b_table.array[107][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert b_table.array[105][0] == "Knuth", "__setitem__ : Not working as expected"
    
    c_table = HashTable(7, 3)
    for key in test_keys:
        c_table[key] = value

    assert c_table.array[0][0] == "Aho" and c_table.array[5][0] == "Kruse" and c_table.array[1][0] == "Standish", "__setitem__ : Not working as expected"
    assert c_table.array[6][0] == "Horowitz" and c_table.array[2][0] == "Langsam" and c_table.array[3][0] == "Sedgewick", "__setitem__ : Not working as expected"
    assert c_table.array[4][0] == "Knuth", "__setitem__ : Not working as expected"


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


def Test_Main():
    hash_test()
    __setitem__test()
    __getitem__test()
    __contains__test()


Test_Main()