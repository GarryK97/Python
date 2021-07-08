from Task1 import Array_Based_List

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

def __init__test():
    """
    Tests __init__ function
    :complexity: O(1)
    """
    print("\n===Testing __init__ function===")
    a_list = Array_Based_List(50)  # Test Valid sizes, should be successful
    b_list = Array_Based_List(30)
    try:  # Test Invalid sizes, should cause AssertionError
        c_list = Array_Based_List(-1)
        d_list = Array_Based_List(51)
        e_list = Array_Based_List(0)
        raise Exception("__init__ : Invalid size accepted")  # If above lines do not cause error, below lines will be executed, meaning failed
        # raising Exception to avoid collision with AssertionError
    except AssertionError:
        pass  # because I defined the assertion errors
        
    print_Result(True)  # If above lines do not cause error, means test passed

def __str__test(empty_list, normal_list, full_list):
    """
    Test __str__ function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :complexity: O(N)
    """
    print("\n===Testing __str__ function===")
    assert str(empty_list) == "", "__str__ : Empty list failed"
    assert str(normal_list) == "0\n1\n2\n3\n4\n5\n6\n", "__str__ : Normal list failed"  # Should be successful

    a_str = ""
    for i in range(20):
        a_str += str(i) + "\n"
    assert str(full_list) == a_str, "__str__ : Full list failed"

    print_Result(True)  # If above lines do not cause error,

def __len__test(empty_list, normal_list, full_list):
    """
    Tests __len__ function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :complexity: O(1)
    """
    print("\n===Testing __len__ function===")
    assert len(empty_list) == 0 and len(normal_list) == 7 and len(full_list) == 20, "__len__ failed, not working as expected"

    print_Result(True)  # If no error

def __contains__test(empty_list, normal_list, full_list):
    """
    Tests __contains__ function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :complexity: O(N)
    """
    print("\n===Testing __contains__ function===")
    assert not (0 in empty_list), "Invalid query failed : __contains__ not working as expected"

    assert 6 in normal_list, "Valid query failed : __contains__ not working as expected"
    assert not (9 in normal_list), "Invalid query failed : __contains__ not working as expected"

    assert 16 in full_list, "Valid query failed : __contains__ not working as expected"
    assert not (20 in full_list), "invalid query failed : __contains__ not working as expected"

    print_Result(True)

def is_index_inbound_test(empty_list, normal_list, full_list):
    """
    Tests is_index_inbound function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :complexity: O(1)
    """
    print("\n===Testing is_index_inbound function===")
    assert not empty_list.is_index_inbound(0), "is_index_inbound(): Empty list failed, not working as expected"
    assert not empty_list.is_index_inbound(-1), "is_index_inbound(): Empty list failed, not working as expected"

    assert normal_list.is_index_inbound(6), "is_index_inbound(): Valid index failed, not working as expected"
    assert not normal_list.is_index_inbound(7), "is_index_inbound(): Invalid index failed, Positive invalid index accepted"
    assert not normal_list.is_index_inbound(-8), "is_index_inbound(): Invalid index failed, Negative invalid index accepted"

    assert full_list.is_index_inbound(9), "is_index_inbound(): Valid index failed, not working as expected"
    assert not full_list.is_index_inbound(20), "is_index_inbound(): Invalid index failed, Positive invalid index accepted"
    assert not full_list.is_index_inbound(-21), "is_index_inbound(): Invalid index failed, Negative invalid index accepted"

    print_Result(True)  # If no error

def __getitem__test(empty_list, normal_list, full_list):
    """
    Tests __getitem__ function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :precondition: __len__ must have no errors
    :complexity: O(1)
    """
    print("\n===Testing __getitem__ function===")

    assert normal_list[6] == 6 and normal_list[2] == 2, "Normal list failed : __getitem__ not working as expected"  # Should not cause any error
    try:
        pos_invalid_index = len(normal_list)
        normal_list[pos_invalid_index]  # Should cause IndexError
        empty_list[pos_invalid_index]
        raise AssertionError("__getitem__ : Empty list or Normal list failed, Positive Invalid index accepted")
        # If above lines do not cause error, the line will be executed, meaning failure
    except IndexError:
        pass    # because I defined the IndexError
    try:
        neg_invalid_index = -len(normal_list) -1
        normal_list[neg_invalid_index]  # Should cause IndexError
        empty_list[neg_invalid_index]
        raise AssertionError("__getitem__ : Empty list or Normal list failed, Negative Invalid index accepted")
    except IndexError:
        pass

    assert full_list[14] == 14 and full_list[-2] == 18, "Full list failed : __getitem__ not working as expected"
    try:
        pos_invalid_index = len(full_list)
        full_list[pos_invalid_index]  # Should cause IndexError
        raise AssertionError("__getitem__ : Full list failed, Positive Invalid index accepted")  # Same mechanism
    except IndexError:
        pass
    try:
        neg_invalid_index = -len(full_list)-1
        full_list[neg_invalid_index]
        raise AssertionError("__getitem__ : Full list failed, Negative Invalid index accepted")
    except IndexError:
        pass

    print_Result(True)  # If all okay, print test passed
        
def __setitem__test(empty_list, normal_list, full_list):
    """
    Test __setitem__ function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :precondition: copy(), __len__ must have no errors
    :complexity: O(N) , including copy()
    """
    item = 41  # temporary item for testing
    full_listcopy = full_list.copy()
    normal_listcopy = normal_list.copy()    # Making copies not to affect the original list
    empty_listcopy = empty_list.copy()

    print("\n===Testing __setitem__ function===")
    n_validindex = len(normal_listcopy) // 2  # Choosing the middle index
    normal_listcopy[n_validindex] = item    # Should have no error and set item
    assert normal_listcopy[n_validindex] == item, "Valid index failed : __setitem__ not working as expected"  # if __setitem__ not working properly, this line will return True

    try:
        invalid_index = len(normal_listcopy) + 1
        normal_listcopy[invalid_index] = item  # Should cause IndexError
        empty_listcopy[invalid_index] = item
    except IndexError:
        pass    # because I defined the IndexError

    full_listcopy[16] = item
    assert full_listcopy[16] == item, "Valid index failed : __setitem__ not working as expected"
    try:
        neg_invalid_index = -len(full_listcopy)-1
        full_listcopy[neg_invalid_index] = item  # Should cause IndexError
        raise AssertionError("Negative invaild index failed : __setitem__ accepted it")
    except IndexError:  # Defined error
        pass

    print_Result(True)
        
def __eq__test(normal_list):
    """
    Tests __eq__ function
    :param normal_list: Non-empty list, length = 7
    :precondition: copy(), append(), __len__ must have no error
    :complexity: O(N), including copy()
    """
    ### Test Cases ###
    equal_list = normal_list.copy()  # Making a copy of the list
    n_equal_list = Array_Based_List(normal_list.size)  # Not equal list, but with the same length
    for i in range(len(normal_list)):
        n_equal_list.append(-1)  # Adding any element (Need to be different with normal list elements)
    n_equal_list_dl = Array_Based_List(normal_list.size)  # Not equal list with different length
    for i in range(len(normal_list)-1):
        n_equal_list_dl.append(-1)  # Same with the above

    ### Test ###
    print("\n===Testing __eq__ function===")
    assert normal_list == equal_list, "__eq__ : Equal list failed"  # If not equal, test failed
    assert not normal_list == n_equal_list, "__eq__ : Not equal list with the same length failed"   # If return True, test failed
    assert not normal_list == n_equal_list_dl, "__eq__ : Not equal list with different length failed"  # If return True, test failed

    print_Result(True)

def is_full_test(empty_list, not_full_list, full_list):
    """
    Tests is_full function
    :param empty_list: empty list
    :param not_full_list: list that is not full
    :param full_list: list that is full
    :complexity: O(1)
    """
    print("\n===Testing is_full function===")
    assert not empty_list.is_full(), "is_full() : Empty list failed"  # is_full should return false,
    assert not not_full_list.is_full(), "is_full() : Normal list failed"
    assert full_list.is_full(), "is_full() : Full list failed"  # if is_full not working,

    print_Result(True)

def append_test(empty_list, normal_list, full_list):
    """
    Tests append function
    :param empty_list: empty list
    :param normal_list: non-empty list, length = 7
    :param full_list: full list, length = 20
    :precondition: copy(), __len__, __getitem__ must have no errors
    :complexity: O(N) , including copy()
    """
    ### Test Cases ###
    empty_listcopy = empty_list.copy()  # Making copies not to affect the originals
    normal_listcopy = normal_list.copy()
    full_listcopy = full_list.copy()

    ### Test ###
    print("\n===Testing append_test function===")

    empty_listcopy.append(99)   # Should not cause errors
    assert len(empty_listcopy) == len(empty_list) +1, "Empty list failed : append() not updating the length"
    assert empty_listcopy[-1] == 99, "Empty list failed : append() not working as expected"

    normal_listcopy.append(77)
    assert len(normal_listcopy) == len(normal_list)+1, "Not full list failed : append() not updating the length (self.count)"  # If length remains the same,
    assert normal_listcopy[-1] == 77, "Not full list failed : append() not working as expected"  # If the last element is not appended item,

    try:
        full_listcopy.append(33)  # Should cause error
        raise AssertionError("Full list failed : append() worked")
    except Exception:
        pass  # Because I defined the Exception

    print_Result(True)

def insert_test(empty_list, normal_list, full_list):
    """
    Tests insert function
    :param empty_list: empty list
    :param normal_list: non-full list
    :param full_list: Full list
    :precondition: copy(), __len__, __getitem__ must have no errors
    :complexity: O(N) , including copy()
    """
    ### Test Cases ###
    empty_listcopy = empty_list.copy()
    normal_listcopy = normal_list.copy() # Making copies not to affect the original lists
    full_listcopy = full_list.copy()
    item = 74  # Temporary item for testing

    ### Test ###
    print("\n===Testing insert function===")

    empty_listcopy.insert(len(empty_listcopy), item)  # Should not cause any error, Item must be added to last
    assert empty_listcopy[0] == item, "Empty list failed : insert() not working as expected"  # Item must be added to index 0.

    index = len(normal_listcopy) // 2  # Getting any index of the list, in this case, middle item
    normal_listcopy.insert(index, item)  # Should cause no error
    assert normal_listcopy[index] == item, "Valid index failed : insert() not working as expected" # If the item inserted is not at the index, means something wrong
    for i in range(index):  # Checks if items in front index remain the same
        assert normal_listcopy[i] == normal_list[i], "Valid index failed : insert(), items in front changed"
    for i in range(index+1, len(normal_listcopy)):  # Checks if items behind index remain the same
        assert normal_listcopy[i] == normal_list[i-1], "Valid index failed : insert(), items behind changed"
    try:
        normal_listcopy.insert(len(normal_listcopy)+1, item) # Should cause error
        raise AssertionError("Invalid index failed : insert(invalid_index) worked")  # If above lines do not cause error,
    except IndexError:
        pass  # Because I defined IndexError

    try:
        valid_index = len(full_listcopy // 2)
        full_listcopy.insert(valid_index, item)  # Should cause error
        raise AssertionError("Full list failed : insert() worked")  # If above lines do not cause error,
    except Exception:
        pass  # Defined error

    print_Result(True)

def remove_test(empty_list, normal_list):
    """
    Tests remove function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :precondition: copy(), __getitem__, __len__, append() must have no errors
    :complexity: O(N^2)
    """
    ### Test Cases ###
    empty_listcopy = empty_list.copy()  # Making copies not to affect originals
    normal_listcopy = normal_list.copy()
    test_list = Array_Based_List(5)  # Test case to check if remove() correctly removes the item
    for i in range(4):  # Appending 0,1,2,3
        test_list.append(i)

    ### Test ###
    print("\n===Testing remove function===")
    try:
        empty_listcopy.remove(23)  # Should cause error
        raise AssertionError("Empty list failed : remove() worked")  # If above line does not cause any error,
    except ValueError:  # Ignore ValueError as I defined it
        pass

    item_toremove = normal_list[len(normal_list) // 2]  # Choosing any item for testing, in this case, middle item
    normal_listcopy.remove(item_toremove)  # Should cause no error
    assert len(normal_listcopy) != len(normal_list), "Normal list failed : remove() not updating the length"  # If the length are the same,

    test_list.remove(2)  # Remove 2, so test_list should be 0,1,3
    assert test_list[0] == 0 and test_list[1] == 1 and test_list[2] == 3, "Test list failed : remove() not working as expected"
        
    print_Result(True)

def delete_test(empty_list, normal_list):
    """
    Test delete function
    :param empty_list: Empty list
    :param normal_list: Non-empty list, length = 7
    :precondition: copy(), __len__, __getitem__, append() must have no errors
    :complexity: O(N) , including copy()
    """
    ### Test Cases ###
    empty_listcopy = empty_list.copy()  # Making copies not to affect originals
    normal_listcopy = normal_list.copy()
    test_list = Array_Based_List(5)  # Test case to check if delete() correctly deletes the item at the index
    for i in range(4):  # Appending 0,1,2,3
        test_list.append(i)

    ### Test ###
    print("\n===Testing delete function===")
    try:
        empty_listcopy.delete(0)  # Should cause error
        raise AssertionError("Empty list failed : delete() worked")  # Same mechanism with other test functions
    except IndexError:  # Defined error
        pass

    normal_listcopy.delete(len(normal_listcopy) // 2) # Should cause nor error, Choosing the middle index to delete
    assert len(normal_listcopy) == len(normal_list)-1, "Normal list failed : delete() not updating the length" # Checks if delete() correctly updates the length

    test_list.delete(1)  # Deleting two times to make sure that delete works properly
    test_list.delete(1)  # Now, test_list should have 0,3
    assert test_list[0] == 0 or test_list[1] == 3, "Test list failed : delete() not working as expected"
    
    print_Result(True)

def sort_test(empty_list, normal_list, full_list):
    """
    Tests sort function
    :param empty_list: Empty list
    :param normal_list: Non-empty list
    :param full_list: Full list
    :precondition: copy(), __len__, __getitem__ must have no errors
    :complexity: Average Case : O(N^2)
    """
    ### Test Cases ###
    empty_listcopy = empty_list.copy()  # Making copies not to affect the original lists
    normal_listcopy = normal_list.copy()
    full_listcopy = full_list.copy()

    ### Test ###
    print("\n===Testing sort function===")
    try:
        empty_listcopy.sort(False)  # Should cause error
        empty_listcopy.sort(True)
        raise Exception("Empty list failed : sort() worked")  # Same mechanism with other functions, but raising Exception to avoid collision
    except AssertionError:  # Defined Error
        pass

    normal_listcopy.sort(False)  # Should cause no error
    for i in range(1, len(normal_listcopy)):
        if normal_listcopy[i - 1] > normal_listcopy[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Normal list failed, not working as expected, unsorted elements exist (reverse = False)")
    normal_listcopy.sort(True)  # Should cause no error
    for i in range(1, len(normal_listcopy)):
        if normal_listcopy[i - 1] < normal_listcopy[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Normal list failed, not working as expected, unsorted elements exist (reverse = True)")

    full_listcopy.sort(False)  # Should cause no error
    for i in range(1, len(full_listcopy)):
        if full_listcopy[i - 1] > full_listcopy[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Full list failed, not working as expected, unsorted elements exist (reverse = False)")
    full_listcopy.sort(True)  # Should cause no error
    for i in range(1, len(full_listcopy)):
        if full_listcopy[i - 1] < full_listcopy[i]:  # Checking if unsorted elements exist
            raise AssertionError("sort() : Full list failed, not working as expected, unsorted elements exist (reverse = True)")
        
    print_Result(True)

def __iter__test(empty_list, normal_list, full_list):
    """
    Tests __iter__ function (Testing whether the class is iterable)
    :param empty_list: Empty list
    :param normal_list: Non-empty list
    :param full_list: Full list
    :precondition: __getitem__, __len__ must have no error
    :complexity: O(N)
    """
    print("\n===Testing __iter__ function===")

    e_itr = iter(empty_list)  # Should cause no error here.
    try:
        next(e_itr)  # Should cause StopIteration error as no elements exist
        raise AssertionError("__iter__ : Empty list failed, next() worked")  # If above does not cause error,
    except StopIteration:  # Defined error
        pass

    n_itr = iter(normal_list)
    assert next(n_itr) == normal_list[0] and next(n_itr) == normal_list[1], "Normal list failed : __iter__ not working as expected"

    f_itr = iter(full_list)
    for i in range(len(full_list)-1):  # next(f_itr) until it reaches the last element to see if Iteration stops when reached the end
        next(f_itr)
    assert next(f_itr) == full_list[-1], "Full list failed : __iter__ not working as expected" # next(f_itr) in this statement should be full_list[-1] (last element).
    try:
        next(f_itr)  # Now, next(f_itr) should cause StopIteration error.
        raise AssertionError("Full list failed : __iter__ or StopIteration not working properly")  # If above line does not cause error,
    except StopIteration:
        pass

    ### Testing for loop ###
    for_loop_sum = 0
    for i in range(len(normal_list)):
        for_loop_sum += normal_list[i]
    itr_for_loop_sum = 0
    for item in normal_list:
        itr_for_loop_sum += item
    assert for_loop_sum == itr_for_loop_sum, "Iteration For loop failed : iter() or next() not working as expected"  # Both must do the same task if __iter__ has no error

    # Below lines should work if above tests passed
    for_loop_sum = 0
    for i in range(len(full_list)):  # Normal for loop testing
        for_loop_sum += full_list[i]
    itr_forloop_sum = 0
    for item in full_list:  # iteration for loop testing
        itr_forloop_sum += item
    assert for_loop_sum == itr_forloop_sum, "Iteration For loop failed : iter() or next() not working as expected"

    print_Result(True)


def copy_test(empty_list, normal_list, full_list):
    """
    Tests copy function
    :param empty_list: Empty list
    :param normal_list:  Non-empty list, length = 7
    :param full_list: Full list, length = 20
    :precondition: __eq__ must have no error
    :complexity: O(N) , including copy()
    """
    is_successful = True
    print("\n===Testing copy function===")
    empty_listcopy = empty_list.copy()
    normal_listcopy = normal_list.copy()
    full_listcopy = full_list.copy()
    assert empty_list == empty_listcopy, "copy() : Empty list failed, not working as expected"
    assert normal_listcopy == normal_listcopy, "copy() : Normal list failed, not working as expected"
    assert full_listcopy == full_list, "copy() : Full list failed, not working as expected"

    print_Result(True)


def test_Functions():
    """""""""""""""""""""
    Main function for testing
    :precondtion: 1. Test cases must consist of only int type elements, due to few functions. e.g.) sort
                  2. Array_based_List class objects should be used for this function.
                  3. append() must have no error to set the test cases
    :complexity: O(N)
    """""""""""""""""""""
    ### Making Test Cases ###
    normal_list = Array_Based_List(20)
    for i in range(7):  # Making a list with elements
        normal_list.append(i)
    empty_list = Array_Based_List(20) # Empty list
    full_list = Array_Based_List(20) # Full list
    for i in range(20):
        full_list.append(i)

    ### Test Functions ###
    __init__test()
    __str__test(empty_list, normal_list, full_list)
    __len__test(empty_list, normal_list, full_list)
    __contains__test(empty_list, normal_list, full_list)
    is_index_inbound_test(empty_list, normal_list, full_list)
    __getitem__test(empty_list, normal_list, full_list)
    __setitem__test(empty_list, normal_list, full_list)
    __eq__test(normal_list)
    is_full_test(empty_list, normal_list, full_list)
    append_test(empty_list, normal_list, full_list)
    insert_test(empty_list, normal_list, full_list)
    remove_test(empty_list, normal_list)
    delete_test(empty_list, normal_list)
    sort_test(empty_list, normal_list, full_list)
    __iter__test(empty_list, normal_list, full_list)
    copy_test(empty_list, normal_list, full_list)


test_Functions()