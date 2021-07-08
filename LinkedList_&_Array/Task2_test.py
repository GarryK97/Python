from Task2 import Array_Based_List


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

def print_Length_Size(a_list, is_after):
    """
    Prints the current length and max size of the list (array)
    :param a_list: any Array_Based_List object
    :param is_after: bool that determines to print Before or After
    :complexity: O(1)
    """
    if is_after:
        print("After : length = " + str(len(a_list)), "Maximum size = " + str(a_list.size))
    else:
        print("Before : length = " + str(len(a_list)), "Maximum size = " + str(a_list.size))

def append_makedynamic_test():
    """
    Tests if modified append function now works with full lists, focusing on whether make_dynamic properly working or not
    This function must work properly to test other functions, as other functions require append() function for test cases
    :return: is_successful (Test passed or not)
    :precondition: append function itself must have no error (it means without make_dynamic(), should work properly.)
                    __getitem__ must have no error
    :complexity: O(1)
    """
    print("\n===Testing append function===")

    print("..Testing Normal list..")
    Normal_list = Array_Based_List()
    for i in range(13):  # Simply making non-empty list with sufficient available spaces
        Normal_list.append(i)  # Should cause no error
    Normal_list.append(15)  # Should cause no error
    Normal_list.append(23)

    assert Normal_list.size == 20, "Normal list failed : Size of normal list is different from Base size"  # If Normal_list.size is changed (Means something wrong)
    assert Normal_list[-2] == 15 and Normal_list[-1] == 23, "Normal list failed : append() not working as expected"  # Checking if elements are appended correctly

    print("..Testing Full list..")
    Full_list = Array_Based_List()  # Testcase (Full list with base size 20)
    for i in range(20):  # Appending 20 elements which is the maximum elements for the base size
        Full_list.append(i)
    print_Length_Size(Full_list, False)

    Full_list.append(55)  # Should cause no error and the size must be 40
    Full_list.append(47)
    print_Length_Size(Full_list, True)

    assert Full_list.size == 40, "Full list failed : Maximum size is different from expectation"
    assert Full_list[-2] == 55 or Full_list[-1] == 47, "Full list failed : append() not working as expected" # Checking if elements are appended correctly

    print("..Testing Bigsize list..")
    Bigsize_list = Array_Based_List()  # Testcase (List with a big size)
    print_Length_Size(Bigsize_list, False)

    for i in range(800):  # Appending more than base size, so size must be bigger than 20
        Bigsize_list.append(i)  # Based on my code, the maximum size of the array should be 1280
    print_Length_Size(Bigsize_list, True)

    assert Bigsize_list.size == 1280, "Bigsize list failed : Maximum size is different from expectation"
    assert Bigsize_list[-2] == 798 or Bigsize_list[-1] == 799, "Bigsize list failed : append() not working as expected" # Checking if elements are appended correctly

    print_Result(True)  # if no error, below lines will be executed
    return True  # Required to test other testing functions

def insert_makedynamic_test(Empty_list, Normal_list, Full_list, Full_Bigsize_list):
    """
    Tests modified insert() function, focusing on if make_dynamic() properly working
    :param Empty_list: Empty list with base size
    :param Normal_list: Non-empty list with base size
    :param Full_list: Full list with base size
    :param Full_Bigsize_list: Full Bigsize list (> 640)
    :precondition: insert(), copy(), __getitem__, __len__ must have no errors
    :complexity: O(N) , including copy()
    """
    Empty_listcopy = Empty_list.copy()  # Making copies not to affect the original test cases
    Normal_listcopy = Normal_list.copy()
    Full_listcopy = Full_list.copy()
    Full_Bigsize_listcopy = Full_Bigsize_list.copy()
    item = 77  # Temporary item to test insert()

    print("\n===Testing insert function===")
    print("..Testing Empty list..")
    Empty_listcopy.insert(0, item)  # Should cause no error, item must be appended at the last
    assert Empty_listcopy[0] == item, "Empty list failed : insert() not working"  # if item is not inserted properly, means error

    print("..Testing Normal list..")
    index = len(Normal_listcopy) // 2  # Choosing any index for testing
    Normal_listcopy.insert(index, item)  # Should cause no error
    assert Normal_listcopy[index] == item, "Normal list failed : insert() not working as expected"  # If item is not at index, means something wrong
    for i in range(index):  # Checks if items in front index remain the same
        assert Normal_listcopy[i] == Normal_list[i], "Normal list failed : insert(), items in front changed"
    for i in range(index+1, len(Normal_listcopy)):  # Checks if items behind index remain the same
        assert Normal_listcopy[i] == Normal_list[i-1], "Normal list failed : insert(), items behind changed"

    print("..Testing Full list..")
    index = len(Full_listcopy) // 2  # Choosing any index for testing
    print_Length_Size(Full_listcopy, False)

    Full_listcopy.insert(index, item)  # Should cause no error, size must be enlarged to 40
    print_Length_Size(Full_listcopy, True)
    assert Full_listcopy[index] == item, "Full list failed : insert() not working as expected"  # If item is not at index, means something wrong
    assert Full_listcopy.size == Full_list.size * 2, "Full list failed : Maximum size is different from expectation"  # If the increased size is not original size * 2,
    for i in range(index):  # Checks if items in front index remain the same
        assert Full_listcopy[i] == Full_list[i], "Full list failed : insert(), items in front changed"
    for i in range(index+1, len(Full_listcopy)):  # Checks if items behind index remain the same
        assert Full_listcopy[i] == Full_list[i-1], "Full list failed : insert(), items behind changed"

    print("..Testing Full Bigsize list..")
    index = len(Full_Bigsize_listcopy) // 2
    print_Length_Size(Full_Bigsize_listcopy, False)

    Full_Bigsize_listcopy.insert(index, item)  # Should have no error, size must be enlarged
    print_Length_Size(Full_Bigsize_listcopy, True)
    assert Full_Bigsize_listcopy[index] == item, "Full Bigsize list failed : insert() not working as expected"
    assert Full_Bigsize_listcopy.size == Full_Bigsize_list.size * 2, "Full Bigsize list failed : Maximum size is different from expectation"  # If the increased size is not original size * 2,
    for i in range(index):  # Checks if items in front index remain the same
        assert Full_Bigsize_listcopy[i] == Full_Bigsize_list[i], "Full Bigsize list failed : insert(), items in front changed"
    for i in range(index+1, len(Full_Bigsize_listcopy)):  # Checks if items behind index remain the same
        assert Full_Bigsize_listcopy[i] == Full_Bigsize_list[i-1], "Full Bigsize list failed : insert(), items behind changed"

    print_Result(True)

def remove_makedynamic_test(Empty_list, Bigsize_list, Full_Bigsize_list):
    """
    Tests modified remove function, focusing on whether make_dynamic() working or not
    ( Because original remove function itself is tested in Task1_test.py)
    :param Empty_list: Empty list
    :param Bigsize_list: Bigsize list (> 640) with available spaces
    :param Full_Bigsize_list: Full Bigsize list
    :precondition: remove(), copy(), __getitem__, __len__ must have no errors
    :complexity: Average case : O(N^2), including remove() function
    """
    Empty_listcopy = Empty_list.copy()
    Bigsize_listcopy = Bigsize_list.copy()  # Making copies not to affect the originals
    Full_Bigsize_listcopy = Full_Bigsize_list.copy()

    print("\n===Testing remove function===")
    try:
        print("..Testing Empty list..")
        Empty_listcopy.remove(5)  # Should cause ValueError as no elements exist
        raise AssertionError("Empty list failed : remove() worked")  # If above does not cause error,
    except ValueError:  # Defined error
        pass

    print("..Testing Bigsize list..")
    print_Length_Size(Bigsize_listcopy, False)

    for i in range(len(Bigsize_listcopy)-10):
        item = Bigsize_listcopy[-1]  # Temporary item for testing, last element of the list
        Bigsize_listcopy.remove(item)  # Item removed until 10 elements left, then, max size should be decreased.
    print_Length_Size(Bigsize_listcopy, True)

    available_space = Bigsize_listcopy.size - len(Bigsize_listcopy)
    assert not len(Bigsize_listcopy) < (available_space // 8), "Bigsize list failed : Maximum size is different from expectation"
    # If the length is less than available space / 8, it means maximum size is not decreased properly

    print("..Testing Full Bigsize list")
    print_Length_Size(Full_Bigsize_listcopy, False)

    for i in range(len(Full_Bigsize_listcopy)-50):
        item = Full_Bigsize_listcopy[-1]    # Similar process above
        Full_Bigsize_listcopy.remove(item)  # Remove item until 50 elements left
    print_Length_Size(Full_Bigsize_listcopy, True)

    available_space = Full_Bigsize_listcopy.size - len(Full_Bigsize_listcopy)
    assert not len(Full_Bigsize_listcopy) < (available_space // 8), "Full Bigsize list failed : Maximum size is different from expectation"
    # If the length is less than available space / 8, it means maximum size is not decreased properly

    print_Result(True)
    
def delete_makedynamic_test(Empty_list, Bigsize_list, Full_Bigsize_list):
    """
    Tests modified delete function, focusing on whether make_dynamic() working or not
    :param Empty_list: Empty list
    :param Bigsize_list: Bigsize list ( > 640 ) with available spaces
    :param Full_Bigsize_list: Full Bigsize list ( > 640)
    :precondition: delete(), copy(), __len__ must have no errors
    :complexity: O(N)
    """
    Empty_listcopy = Empty_list.copy()  # Making copies not to affect the originals
    Bigsize_listcopy = Bigsize_list.copy()
    Full_Bigsize_listcopy = Full_Bigsize_list.copy()

    print("\n===Testing delete function===")
    try:
        print("..Testing Empty list..")
        Empty_listcopy.delete(0)  # Should cause IndexError as no elements exist
        raise AssertionError("Empty list failed : delete() worked")  # If above does not cause an error,
    except IndexError:  # Defined error
        pass

    print("..Testing Bigsize list..")
    print_Length_Size(Bigsize_listcopy, False)

    for i in range(len(Bigsize_listcopy) - 30):
        Bigsize_listcopy.delete(0)  # Item deleted until 30 elements left, then, max size should be decreased.
    print_Length_Size(Bigsize_listcopy, True)

    available_space = Bigsize_listcopy.size - len(Bigsize_listcopy)
    assert not len(Bigsize_listcopy) < (available_space // 8), "Bigsize list failed : Maximum size is different from expectation"
    # If the length is less than available space / 8, it means maximum size is not decreased properly

    print("..Testing Full Bigsize list")
    print_Length_Size(Full_Bigsize_listcopy, False)

    for i in range(len(Full_Bigsize_listcopy) - 80):
        Full_Bigsize_listcopy.delete(0)  # item deleted until 80 elements left
    print_Length_Size(Full_Bigsize_listcopy, True)

    available_space = Full_Bigsize_listcopy.size - len(Full_Bigsize_listcopy)
    assert not len(Full_Bigsize_listcopy) < (available_space // 8), "Full Bigsize list failed : Maximum size is different from expectation"
    # If the length is less than available space / 8, it means maximum size is not decreased properly

    print_Result(True)


def test_Functions():
    """""""""
    Main function for Testing
    :complexity: O(N^2)
    """""""""
    if append_makedynamic_test():  # append function test must pass to set test cases
        ### Test Cases ###
        Empty_list = Array_Based_List()  # Empty list with base size
        Normal_list = Array_Based_List()  # a normal list with base size, with sufficient available space
        for i in range(10):
            Normal_list.append(i)
        Full_list = Array_Based_List()  # Full list with base size, without any available space
        for i in range(20):
            Full_list.append(i)
        Bigsize_list = Array_Based_List()  # Bigsized-list with size 1280, with available spaces
        for i in range(900):
            Bigsize_list.append(i)
        Full_Bigsize_list = Array_Based_List()  # Full Bigsized-list with size 1280
        for i in range(1280):
            Full_Bigsize_list.append(i)

        ### Test Functions ###
        insert_makedynamic_test(Empty_list, Normal_list, Full_list, Full_Bigsize_list)
        remove_makedynamic_test(Empty_list, Bigsize_list, Full_Bigsize_list)
        delete_makedynamic_test(Empty_list, Bigsize_list, Full_Bigsize_list)
        """ 
        In Task2 test, I only included these test functions because, I copied the same class in Task1 and modified it for Task2.
        So, all the functions can be tested in Task1_test.py and I assumed that functions are working properly.
        Modified functions are all tested in this test_Functions(), i.e) append, insert, remove, delete
        I focused on testing whether the size is dynamic, not testing the function itself, due to above reasons
        Did not make test function for make_dynamic() because it is tested together inside other test functions
        If make_dynamic() is not working properly, all the test functions will give error
        """


test_Functions()