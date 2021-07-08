from Task4 import arraylist_readfile, linkedlist_readfile

### Test Cases ###
file1 = "test1.txt"  # text file with 0 1 2 3 4 5
file2 = "test2.txt"  # text file with 1 3 5 7 9
file3 = "test3.txt"  # text file with 11 22 33 44 55

def arraylist_readfile_test(file1, file2, file3):
    """
    Tests arraylist_readfile() function
    :param file1: test1.txt (name only)
    :param file2: test2.txt (name only)
    :param file3: test3.txt (name only)
    :precondition: __getitem__ of Array_Based_List must have no error
    :complexity: O(N)
    """
    print("\n===Testing Array_Based_List file reading ===")
    array_list = arraylist_readfile(file1)
    for i in range(6):
        assert int(array_list[i]) == i, "Reading file to array_list seems not working as expected"

    array_list = arraylist_readfile(file2)
    index = 0
    for i in range(1, 10, 2):
        assert int(array_list[index]) == i, "Reading file to array_list seems not working as expected"
        index += 1

    array_list = arraylist_readfile(file3)
    index = 0
    for i in range(11, 56, 11):
        assert int(array_list[index]) == i, "Reading file to array_list seems not working as expected"
        index += 1
    
    print("Test Passed")

def linkedlist_readfile_test(file1, file2, file3):
    """
    Tests linkedlist_readfile() function
    :param file1: test1.txt (name only)
    :param file2: test2.txt (name only)
    :param file3: test3.txt (name only)
    :precondition: __getitem__ of Linked List must have no error
    :complexity: O(N)
    """
    print("\n===Testing Linked List file reading ===")
    linked_list = linkedlist_readfile(file1)
    for i in range(6):
        assert int(linked_list[i]) == i, "Reading file to linked_list seems not working as expected"

    linked_list = linkedlist_readfile(file2)
    index = 0
    for i in range(1, 10, 2):
        assert int(linked_list[index]) == i, "Reading file to linked_list seems not working as expected"
        index += 1

    linked_list = linkedlist_readfile(file3)
    index = 0
    for i in range(11, 56, 11):
        assert int(linked_list[index]) == i, "Reading file to linked_list seems not working as expected"
        index += 1

    print("Test Passed")


### Main ###
arraylist_readfile_test(file1, file2, file3)
linkedlist_readfile_test(file1, file2, file3)
