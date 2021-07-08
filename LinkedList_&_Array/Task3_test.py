from Task3 import LinkedList


def print_Result(a_bool):
    """
    Prints the result of a test
    :param a_bool: test result (bool type)
    :complexity: O(1)
    """
    if a_bool:
        print("Result : Test Successful")
    else:
        print("Result : Test Failed")

def append_test():
    """
    Test append function. This test must pass to make test cases for other test functions
    :return: bool value, test passed or failed
    :precondition: __getitem__, __len__ must have no error
    :complexity: O(N^2), including __getitem__
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    normal_list = LinkedList()  # Non-empty list with length 5
    big_list = LinkedList()  # Non-empty list, with big size, 50
    for i in range(5):
        normal_list.append(i)  # normal_list = [0,1,2,3,4]
    for i in range(50):
        big_list.append(i)  # big_list = [0,1,2,3,4,5,...,49]
        
    ### Test ###
    print("\n===Testing append function===")
    empty_list.append(11)
    empty_list.append(22)
    assert empty_list[0] == 11 and empty_list[1] == 22, "append() : Empty list failed, not working as expected"
    assert len(empty_list) == 2, "append() :  Empty list failed, not updating length correctly"
    
    original_length = len(normal_list)
    normal_list.append(17)
    normal_list.append(34)
    for num in range(original_length):
        assert normal_list[num] == num, "append() : Normal list failed, seems affecting others"
    assert normal_list[-2] == 17 and normal_list[-1] == 34, "append() : Normal list failed, not working as expected"
    assert len(normal_list) == original_length +2, "append() : Normal list failed, not updating length correctly"
    
    original_length = len(big_list)
    big_list.append(30)
    big_list.append(24)
    for num in range(original_length):
        assert big_list[num] == num, "append() : Big list failed, seems affecting others"
    assert big_list[-2] == 30 and big_list[-1] == 24, "append() : Big list failed, not working as expected"
    assert len(big_list) == original_length +2, "append() : Big list failed, not updating length correctly"

    print_Result(True)  # If above lines cause error, below lines will not be executed
    return True
    

def __str__test(empty_list, normal_list, big_list):
    """
    Tests __str__ function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :complexity: O(N)
    """
    ### Test ###
    print("\n===Testing __str__ function===")
    
    assert str(empty_list) == "", "__str__ : Empty list failed, not working as expected"
    assert str(normal_list) == "0\n1\n2\n3\n4\n", "__str__ : Normal list failed, not working as expected"

    temp_str = ""
    for i in range(50):
        temp_str += str(i) + "\n"
    assert str(big_list) == temp_str, "__str__ : Big list failed, not working as expected"
    
    print_Result(True)  # if above lines cause error, this line will not be executed.

def __len__test():
    """
    Tests __len__ function
    :precondition: append() must have no error
    :complexity: O(1)
    """
    ### Test Cases ###
    length0_list = LinkedList()
    length7_list = LinkedList()
    length20_list = LinkedList()
    for i in range(7):
        length7_list.append(i)
    for i in range(20):
        length20_list.append(i)

    ### Test ###
    print("\n===Testing __len__ function===")
    assert len(length0_list) == 0 and len(length7_list) == 7 and len(length20_list) == 20, "__len__ : not working as expected"

    print_Result(True)  # Same with the other functions

def is_empty_test(empty_list, normal_list, big_list):
    """
    Tests is_empty() function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :complexity: O(1)
    """
    ### Test ###
    print("\n===Testing is_empty() function===")
    assert empty_list.is_empty(), "is_empty() : Empty list failed"
    assert not normal_list.is_empty(), "is_empty() : Normal list failed"
    assert not big_list.is_empty(), "is_empty() : Big list failed"

    print_Result(True)

def __contains__test(empty_list, normal_list, big_list):
    """
    Tests __contains__ function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :complexity: O(N)
    """
    ### Test ###
    print("\n===Testing __contains__ function===")
    assert not (0 in empty_list), "__contains__ : Empty list failed, not working as expected"

    assert (3 in normal_list), "__contains__ : Normal list failed, valid query not found"
    assert not (10 in normal_list), "__contains__ : Normal list failed, invalid query found"

    assert (34 in big_list), "__contains__ : Big list failed, valid query not found"
    assert not (100 in big_list), "__contains__ : Big list failed, invalid query found"

    print_Result(True)

def is_inbound_test(empty_list, normal_list, big_list):
    """
    Tests is_inbound function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :precondition: append() must have no error
    :complexity: O(1)
    """
    ### Test ###
    print("\n===Testing is_inbound() function===")
    assert not empty_list.is_inbound(0), "is_inbound() : Empty list failed, invalid index accepted"

    assert normal_list.is_inbound(4), "is_inbound() : Normal list failed, positive valid index not accepted"
    assert not normal_list.is_inbound(5), "is_inbound() : Normal list failed, positive invalid index accepted"
    assert normal_list.is_inbound(-5), "is_inbound() : Normal list failed, negative valid index not accepted"
    assert not normal_list.is_inbound(-6), "is_inbound() : Normal list failed, negative invalid index accepted"

    assert big_list.is_inbound(38), "is_inbound() : Big list failed, positive valid index not accepted"
    assert not big_list.is_inbound(52), "is_inbound() : Big list failed, positive invalid index accepted"
    assert big_list.is_inbound(-50), "is_inbound() : Big list failed, negative valid index not accepted"
    assert not big_list.is_inbound(-51), "is_inbound() : Big list failed, negative invalid index accepted"

    print_Result(True)

def __getitem__test(empty_list, normal_list, big_list):
    """
    Tests __getitem__ function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :complexity: O(N)
    """
    ### Test ###
    print("\n===Testing __getitem__ function")
    try:
        empty_list[0]  # Should cause IndexError
        raise AssertionError("__getitem__ : Empty list failed, empty_list[0] worked")  # If this line executes, means test failed
    except IndexError:  # Defined error
        pass
    
    assert normal_list[2] == 2 and normal_list[4] == 4, "__getitem__ : Normal list failed, not working as expected"
    try:
        normal_list[5]  # Should cause IndexError
        normal_list[-6]
        raise AssertionError("__getitem__ : Normal list failed, cannot catch IndexError")
    except IndexError:
        pass
    
    assert big_list[30] == 30 and big_list[47] == 47, "__getitem__ : Big list failed, not working as expected"
    try:
        big_list[54]  # Should cause IndexError
        big_list[-53]
        raise AssertionError("__getitem__ : Big list failed, cannot catch IndexError")
    except IndexError:
        pass

    print_Result(True)

def get_node_test(empty_list, normal_list, big_list):
    """
    Tests get_node() function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :complexity: O(N)
    """
    print("\n===Testing get_node function===")
    try:
        empty_list.get_node(0)  # should cause IndexError
        raise AssertionError("get_node() : Empty list failed, get_node(0) worked")  # If above does not cause error,
    except IndexError:  # Defined Error
        pass

    normal_node4 = normal_list.get_node(4)  # Should cause no error
    normal_node3 = normal_list.get_node(3)
    assert normal_node3.item == 3, "get_node() : Normal list failed, node item is wrong"  # Checks if node item is correct
    assert normal_node3.next == normal_list.get_node(4), 'get_node() : Normal list failed, node next is wrong'  # Checks if node's next is correct next node
    assert normal_node4.next is None, "get_node() : Normal list failed, last node's next is not None"  # Last node's next must be None

    big_node20 = big_list.get_node(20)
    assert big_node20.item == 20, "get_node() : Big list failed, node item is wrong"
    assert big_node20.next.next.item == 22, "get_node() : Big list failed, node next seems wrong" # Checking both next and item
    assert big_node20.next == big_list.get_node(21), "get_node() : Big list failed, node next is wrong"
    try:
        big_list.get_node(-51)  # Should cause IndexError
        big_list.get_node(50)
        raise AssertionError("get_node() : Big list failed, cannot catch IndexError")
    except IndexError:  # Defined error
        pass
    print_Result(True)  # If all okay, print result

def __setitem__test():
    """
    Tests __setitem__ function
    :precondition: append(), __getitem__ must have no error
    :complexity: O(N)
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    normal_list = LinkedList()  # Non-empty list with length 5
    big_list = LinkedList()  # Non-empty list, with big size, 50
    for i in range(5):
        normal_list.append(i)  # normal_list = [0,1,2,3,4]
    for i in range(50):
        big_list.append(i)  # big_list = [0,1,2,3,4,5,...,49]

    ### Test ###
    print("\n===Testing __setitem__ function===")
    try:
        empty_list[-1] = 13  # Should cause IndexError
        raise AssertionError("__setitem__ : Empty list failed, empty_list[-1] worked")  # If no error, raise AssertionError
    except IndexError:  # Defined error
        pass

    normal_list[3] = 33  # Should cause no error
    normal_list[-3] = 22  # Equivalent to Normal_list[2] = 22
    assert normal_list[3] == 33 and normal_list[2] == 22, "__setitem__ : Normal list failed, not working as expected"

    big_list[20] = 200
    big_list[43] = 430
    assert big_list[20] == 200 and big_list[43] == 430, "__setitem__ : Big list failed, not working as expected"

    print_Result(True)

def __eq__test():
    """
    Tests __eq__ function
    :precondtion: append() must have no error
    :complexity: O(N)
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    empty_list2 = LinkedList()  # Another Empty list
    testing_list = LinkedList()  # Temporary list for testing
    notequal_list = LinkedList()  # Not equal list, different length
    notequal_list_len = LinkedList()  # Not equal list but same length
    equal_list = LinkedList()  # Equal list
    for i in range(5):
        testing_list.append(i)
        equal_list.append(i)
    for i in range(7):
        notequal_list.append(i)
    for i in range(2, 7):
        notequal_list_len.append(i)

    ### Test ###
    print("\n===Testing __eq__ function===")
    assert empty_list == empty_list2, "__eq__ : Empty list failed, not working as expected"
    assert testing_list == equal_list, "__eq__ : Empty list failed, not working as expected"
    assert not testing_list == notequal_list and not testing_list == notequal_list_len, "__eq__ : Normal list failed, not working as expected"

    print_Result(True)

def insert_test():
    """
    Tests insert() function
    :precondition: append(), __getitem__, __len__ must have no error
    :complexity: O(N^2), including __getitem__
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    normal_list = LinkedList()  # Non-empty list with length 5
    big_list = LinkedList()  # Non-empty list, with big size, 50
    for i in range(5):
        normal_list.append(i)  # normal_list = [0,1,2,3,4]
    for i in range(50):
        big_list.append(i)  # big_list = [0,1,2,3,4,5,...,49]

    ### Test ###
    print("\n===Testing insert function===")
    empty_list.insert(0, 3)  # Should cause no error, item must be added
    empty_list.insert(0, 5)
    assert empty_list[0] == 5 and empty_list[1] == 3, "insert() : Empty list failed, not working as expected"

    normal_list.insert(len(normal_list), 66)  # Should cause no error, item must be added at the last
    normal_list.insert(3 , 33)
    for i in range(3):  # Checking whether item inserted correctly and not affected other elements
        assert normal_list[i] == i, "insert() : Normal list failed, insert() seems affecting front elements"
    assert normal_list[3] == 33, "insert() : Normal list failed, not working as expected"
    for i in range(4, 5):  # Checking if behind elements not affected, i-1 because my insert() pushes elements behind
        assert normal_list[i] == i-1, "insert() : Normal list failed, insert() seems affecting behind elements"
    assert normal_list[6] == 66, "insert() : Normal list failed, insert() not appending correctly"

    big_list.insert(len(big_list), 510)
    big_list.insert(21, 210)
    for i in range(21):  # Checking whether item inserted correctly and not affected other elements
        assert big_list[i] == i, "insert() : Big list failed, insert() seems affecting front elements"
    assert big_list[21] == 210, "insert() : Big list failed, not working as expected"
    for i in range(22, 51):  # Checking if behind elements not affected, i-1 because my insert() pushes elements behind
        assert big_list[i] == i-1, "insert() : Big list failed, insert() seems affecting behind elements"
    assert big_list[51] == 510, "insert() : Big list failed, insert() not appending correctly"

    print_Result(True)

def remove_test():
    """
    Tests remove() function
    :precondition: append(), __getitem__, __len__ must have no error
    :complexity: O(N)
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    normal_list = LinkedList()  # Non-empty list with length 5
    duplicates_list = LinkedList()  # a list that has some duplicates, [1,2,1,2,1,2]
    for i in range(5):
        normal_list.append(i)
    for i in range(3):
        duplicates_list.append(1)
        duplicates_list.append(2)  # Now, duplicates list = [1,2,1,2,1,2]

    ### Test ###
    print("\n===Testing remove() function===")
    try:
        empty_list.remove(0)  # Should cause ValueError
        normal_list.remove(7)
        duplicates_list.remove(3)
        raise AssertionError("remove() : remove() working with non-existing item, cannot catch ValueError")  # if above lines do not cause error,
    except ValueError:  # Defined error
        pass

    normal_list.remove(2)  # Should cause no error, normal_list = [0,1,3,4]
    assert normal_list[1] == 1 and normal_list[2] == 3, "remove() : not working as expected"  # Checking if 2 removed successfully
    assert len(normal_list) == 4, "remove() : not updating the length correctly" # Length should -1 after remove

    duplicates_list.remove(2)
    assert duplicates_list[1] == 1 and duplicates_list[2] == 2, "remove() : not working as expected"  # Checking if the first element removed
    assert len(duplicates_list) == 5, "remove() : not updating the length correctly"

    print_Result(True)


def sort_test():
    """
    Tests sort() function
    :precondition: append(), __getitem__, __len__ must have no error
    :complexity: O(N^2)
    """
    ### Test Cases ###
    empty_list = LinkedList()  # Empty list
    normal_list = LinkedList()  # Non-empty list with length 5
    big_list = LinkedList()  # Non-empty list, with big size, 50
    for i in range(5):
        normal_list.append(i)  # normal_list = [0,1,2,3,4]
    for i in range(50):
        big_list.append(i)  # big_list = [0,1,2,3,4,5,...,49]

    ### Test ###
    print("\n===Testing sort function===")
    try:
        empty_list.sort(False)  # Should cause AssertionError, based on the sort() function
        raise Exception("sort() : Empty list failed, sort() worked")  # raise Exception to avoid AssertionError collision with except statement
    except AssertionError:
        pass

    normal_list.sort(False)  # Should cause no error
    for i in range(1, len(normal_list)):
        if normal_list[i-1] > normal_list[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Normal list failed, not working as expected, unsorted elements exist (reverse = False)")
    normal_list.sort(True)  # Should cause no error
    for i in range(1, len(normal_list)):
        if normal_list[i-1] < normal_list[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Normal list failed, not working as expected, unsorted elements exist (reverse = True)")
        
    big_list.sort(False)  # Should cause no error
    for i in range(1, len(big_list)):
        if big_list[i-1] > big_list[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Big list failed, not working as expected, unsorted elements exist (reverse = False)")
    big_list.sort(True)  # Should cause no error
    for i in range(1, len(big_list)):
        if big_list[i-1] < big_list[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Big list failed, not working as expected, unsorted elements exist (reverse = True)")

    print_Result(True)

def __iter__test(empty_list, normal_list, big_list):
    """
    Tests __iter__ function
    :param empty_list: Empty list without items (length = 0)
    :param normal_list: Non-empty list (length = 5)
    :param big_list: Non-empty list with big size (length = 50)
    :precondition: __len__ must have no error
    :compleixty:
    """
    ### Test ###
    print("\n===Testing __iter__ function===")
    try:
        e_itr = iter(empty_list)  # Should cause no error here.
        next(e_itr)  # Should cause StopIteration error as no elements exist
        raise AssertionError("__iter__ : Empty list failed, next() worked")  # If above does not cause error,
    except StopIteration:  # Defined error
        pass

    n_itr = iter(normal_list)  # Pointing to the Iterator class object, not yet getting an item
    for i in range(5):
        assert next(n_itr) == i, "__iter__ : Normal list failed, not working as expected"  # Should be always true
    try:
        next(n_itr)  # Now should cause StopIteration error
        raise AssertionError("__iter__ : Normal list failed, Iteration not stopping correctly")  # If above not causing error,
    except StopIteration:  # Defined error
        pass

    b_itr = iter(big_list)  # Same process
    for i in range(50):
        assert next(b_itr) == i, "__iter__ : Big list failed, not working as expected"
    try:
        next(b_itr)
        raise AssertionError("__iter__ : Big list failed, Iteration not stopping correctly")
    except StopIteration:  # Defined error
        pass

    # __iter__ can be test by using for loop
    for_loop_sum = 0
    for i in range(len(normal_list)):
        for_loop_sum += normal_list[i]
    itr_for_loop_sum = 0
    for item in normal_list:
        itr_for_loop_sum += item
    assert for_loop_sum == itr_for_loop_sum, "__iter__ : not working as expected, for loop not working"  # Both must do the same task if __iter__ has no error

    for_loop_sum = 0
    for i in range(len(big_list)):
        for_loop_sum += big_list[i]
    itr_for_loop_sum = 0
    for item in big_list:
        itr_for_loop_sum += item
    assert for_loop_sum == itr_for_loop_sum, "__iter__ : not working as expected, for loop not working"  # Same process

    print_Result(True)
    
def test_functions():
    """
    Main function for testing
    :complexity: O(N^2) , due to remove, sort
    """
    if append_test():
        ### Test Cases ###
        empty_list = LinkedList()  # Empty list
        normal_list = LinkedList()  # Non-empty list with length 5
        big_list = LinkedList()  # Non-empty list, with big size, 50
        for i in range(5):
            normal_list.append(i)  # normal_list = [0,1,2,3,4]
        for i in range(50):
            big_list.append(i)  # big_list = [0,1,2,3,4,5,...,49]

        ### Test Functions ###
        __str__test(empty_list, normal_list, big_list)
        __len__test()
        is_empty_test(empty_list, normal_list, big_list)
        __contains__test(empty_list, normal_list, big_list)
        is_inbound_test(empty_list, normal_list, big_list)
        __getitem__test(empty_list, normal_list, big_list)
        get_node_test(empty_list, normal_list, big_list)
        __setitem__test()
        __eq__test()
        insert_test()
        remove_test()
        sort_test()
        __iter__test(empty_list, normal_list, big_list)


test_functions()