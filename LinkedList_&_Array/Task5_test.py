from Task5 import Editor



def convert_line_toindex_test():
    """
    Tests convert_line_toindex() function
    :precondition: test1.txt must be the file as described below.
    :complexity: O(1), because test1.txt must be fixed
    """
    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format
    
    ### Test Cases ###
    pos_valid_line = 3
    neg_valid_line = -3
    pos_invalid_line = len(test1_file.textlist) + 1
    neg_invalid_line = -len(test1_file.textlist) - 1

    ### Test ###
    print("\n===Testing convert_line_toindex===")
    pos_valid_index = test1_file.convert_line_toindex(pos_valid_line)  # Should be 2
    neg_valid_index = test1_file.convert_line_toindex(neg_valid_line)  # Should remain the same, -3
    pos_invalid_index = test1_file.convert_line_toindex(pos_invalid_line)  # Should be not accepted
    neg_invalid_index = test1_file.convert_line_toindex(neg_invalid_line)  # Should be not accepted

    assert pos_valid_index == 2, "convert_line_to_index() : Positive valid line number failed"
    assert neg_valid_index == -3, "convert_line_to_index() : Negative valid line number failed"
    assert pos_invalid_index is None, "convert_line_to_index() : Positive invalid index is not None (Something wrong)"
    assert neg_invalid_index is None, "convert_line_to_index() : Negative invalid index is not None (Something wrong)"

    print("Test Passed")

def insert_test():
    """
    Tests insert() function. I modified insert() for testing, so that I do not have to enter the text input
    :precondition: test1.txt must be as described below
    :complexity: O(1), because test1.txt must be fixed
    """
    def insert(test_file, line_num):
        """
        Inserts a user's text input into the line number (num)
        :param: test_file: Test file which must be object of Editor class
        :param line_num: Line number to insert
        :return: True, if insert successful. False, if failed
        :precondition: convert_line_toindex() must have no error
        :complexity: Best Case : O(1) , Worst Case : O(N) , due to make_dynamic() in insert().
        """
        index = test_file.convert_line_toindex(line_num)  # Convert line_num to index
        if index is not None:  # If conversion successful,
            user_text = "hello"  # Gets user's text input  (Modified)
            test_file.textlist.insert(index, user_text)
            return True
        else:  # index == None means conversion failed (not valid line_num),
            return False

    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format

    ### Test ###
    print("\n===Testing insert===")
    pos_valid_line1 = 1
    pos_valid_line2 = 6
    neg_valid_line = -6
    pos_invalid_line = 0
    neg_invalid_line = 7

    if not insert(test1_file, pos_valid_line1):  # Should cause no error
        raise AssertionError("insert() : Positive valid line number failed")
    assert str(test1_file.textlist) == "hello\n0\n1\n2\n3\n4\n5\n", "insert() : Positive valid line number, Not working as expected"

    if not insert(test1_file, pos_valid_line2):  # Should cause no error
        raise AssertionError("insert() : Positive valid line number failed")
    assert str(test1_file.textlist) == "hello\n0\n1\n2\n3\nhello\n4\n5\n", "insert() : Positive valid line number, Not working as expected"

    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # Resets test1_file, because it is modified in above test
    if not insert(test1_file, neg_valid_line):  # Should cause no error
        raise AssertionError("insert() : Negative valid line number failed")
    assert str(test1_file.textlist) == "hello\n0\n1\n2\n3\n4\n5\n", "insert() : Negative valid line number, Not working as expected"

    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # Resets test1_file, because it is modified in above test
    assert insert(test1_file, pos_invalid_line) is False, "insert() : Positive invalid line number accepted"  # Invalid index should be not accpeted
    assert insert(test1_file, neg_invalid_line) is False, "insert() : Negative invalid line number accepted"

    print("Test Passed")
    
def read_test():
    """
    Tests read() function
    :precondition: test1.txt, test2.txt, test3.txt must be present, but Nosuchfile.txt must not exist.
    :complexity: O(N)
    """
    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format
    
    test2_file = Editor()  # test2.txt has 1,3,5,7,9 in separated line
    test2_file.textlist = test2_file.arraylist_readfile("test2.txt")  # so, test2_file = [1,3,5,7,9] in list format
    
    test3_file = Editor()  # test3.txt has 11,22,33,44,55 in separated line
    test3_file.textlist = test3_file.arraylist_readfile("test3.txt")  # so, test3_file = [11,22,33,44,55] in list format
    
    ### Test ###
    print("\n===Testing read===")
    test1_test = Editor()
    test1_test.read("test1.txt")
    assert test1_test.textlist == test1_file.textlist, "read() : test1.txt, Not working as expected"
    
    test2_test = Editor()
    test2_test.read("test2.txt")
    assert test2_test.textlist == test2_file.textlist, "read() : test2.txt, Not working as expected"

    test3_test = Editor()
    test3_test.read("test3.txt")
    assert test3_test.textlist == test3_file.textlist, "read() : test3.txt, Not working as expected"

    nofile_test = Editor()
    assert not nofile_test.read("Nosuchfile.txt"), "read() : Non-existing file accepted"  # Should be not accepted

    print("Test Passed")

def write_test():
    """
    Tests write() function
    :precondition: all txt files must be as described below
    :complexity: O(1), because all txt files must be fixed
    """
    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format

    test2_file = Editor()  # test2.txt has 1,3,5,7,9 in separated line
    test2_file.textlist = test2_file.arraylist_readfile("test2.txt")  # so, test2_file = [1,3,5,7,9] in list format

    test3_file = Editor()  # test3.txt has 11,22,33,44,55 in separated line
    test3_file.textlist = test3_file.arraylist_readfile("test3.txt")  # so, test3_file = [11,22,33,44,55] in list format

    ### Test ###
    print("\n===Testing write===")
    real_test = Editor()
    for i in range(6):
        real_test.textlist.append(str(i))  # Directly appending 0,1,2,3,4,5 to compare with test1.txt
    real_test.write("real_test.txt")  # Writes textlist in to real_test.txt, file will be added as it is python built-in function (assume it has no error)
    real_test.textlist = real_test.arraylist_readfile("real_test.txt")  # Reading the file again, to check
    assert real_test.textlist == test1_file.textlist, "write() : Test1, Not working as expected"  # If both are different, means something wrong

    real_test = Editor()  # Reset
    for i in range(1, 10, 2):
        real_test.textlist.append(str(i))  # Directly appending 1,3,5,7,9 to compare with test2.txt
    real_test.write("real_test.txt")  # Same process
    real_test.textlist = real_test.arraylist_readfile("real_test.txt")
    assert real_test.textlist == test2_file.textlist, "write() : Test2, Not working as expected"

    real_test = Editor()
    for i in range(11, 56, 11):
        real_test.textlist.append(str(i))  # Directly appending 11,22,33,44,55 to compare with test3.txt
    real_test.write("real_test.txt")  # Same process
    real_test.textlist = real_test.arraylist_readfile("real_test.txt")
    assert real_test.textlist == test3_file.textlist, "write() : Test3, Not working as expected"

    print("Test Passed")
    
def print_test():
    """
    Tests print() function. I modified the print() to return the string immediately to compare
    :precondition: all txt files must be as described below
    :complexity: O(1), because all txt files must be fixed and index are fixed as well
    """
    def _print(testfile, line_num1, line_num2):  # Added _ to avoid collision with original print (python built-in)
        """
        Prints the lines between line_num1 and line_num2
        :param line_num1: Starting line
        :param line_num2: Ending line
        :return: True, if print successful. False, if failed
        :precondition: convert_line_toindex() must have no error
        :complexity: Average Case : O(N), depends on line_num1 and line_num2
        """
        index1 = testfile.convert_line_toindex(line_num1)  # Converts line number to index
        index2 = testfile.convert_line_toindex(line_num2)
        string_toprint = ""
        if index1 is not None and index2 is not None and index1 < index2: # If both conversion successful and index1 < index2
            for index in range(index1, index2+1):  # index2 +1, because for loop is exclusive
                string_toprint += testfile.textlist[index] + "\n"
        return string_toprint  # (Modified)

    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format

    test2_file = Editor()  # test2.txt has 1,3,5,7,9 in separated line
    test2_file.textlist = test2_file.arraylist_readfile("test2.txt")  # so, test2_file = [1,3,5,7,9] in list format

    test3_file = Editor()  # test3.txt has 11,22,33,44,55 in separated line
    test3_file.textlist = test3_file.arraylist_readfile("test3.txt")  # so, test3_file = [11,22,33,44,55] in list format

    ### Test ###
    print("\n===Testing print===")
    assert _print(test1_file, 2, 6) == "1\n2\n3\n4\n5\n", "print() : Test1, Not working as expected"
    assert _print(test1_file, 1, 5) == "0\n1\n2\n3\n4\n", "print() : Test1, Not working as expected"
    assert _print(test1_file, -2, 3) == "4\n5\n0\n1\n2\n", "print() : Test1, Not working as expected"

    assert _print(test2_file, 1, 3) == "1\n3\n5\n", "print() : Test2, Not working as expected"
    assert _print(test2_file, 3, 4) == "5\n7\n", "print() : Test2, Not working as expected"
    assert _print(test2_file, 4, 3) == "", "print() : Test2 Invalid line numbers, Not working as expected"
    # Above statement should return empty string "", because line_num1 > line_num2

    assert _print(test3_file, 2, 3) == "22\n33\n", "print() : Test3, Not working as expected"
    assert _print(test3_file, 3, 3) == "", "print() : Test3 invalid line numbers, Not working as expected"
    assert _print(test3_file, -3, -1) == "33\n44\n55\n", "print() : Test3 Negative line numbers, Not working as expected"

    print("Test Passed")

def delete_test():
    """
    Tests delete() function
    :precondition: all txt files must be as described below
    :complexity: O(1), because all txt files must be fixed
    """
    ### Test file ###
    test1_file = Editor()  # test1.txt has 0,1,2,3,4,5 in separated line
    test1_file.textlist = test1_file.arraylist_readfile("test1.txt")  # so, test1_file = [0,1,2,3,4,5] in list format

    test2_file = Editor()  # test2.txt has 1,3,5,7,9 in separated line
    test2_file.textlist = test2_file.arraylist_readfile("test2.txt")  # so, test2_file = [1,3,5,7,9] in list format

    test3_file = Editor()  # test3.txt has 11,22,33,44,55 in separated line
    test3_file.textlist = test3_file.arraylist_readfile("test3.txt")  # so, test3_file = [11,22,33,44,55] in list format

    ### Test ###
    print("\n===Testing delete===")
    assert test1_file.delete(3), "delete() : Positive Valid line number not accepted"
    assert str(test1_file.textlist) == "0\n1\n3\n4\n5\n", "delete() : Not working as expected"
    assert test1_file.delete(-1), "delete() : Negative Valid line number not accepted"
    assert str(test1_file.textlist) == "0\n1\n3\n4\n", "delete() : Not working as expected"

    assert not test2_file.delete(0), "delete() : Line number 0 is accepted"
    assert test2_file.delete(-4), "delete() : Negative valid line number not accepted"
    assert str(test2_file.textlist) == "1\n5\n7\n9\n", "delete() : Not working as expected"

    assert not test3_file.delete(-6), "delete() : Negative Invalid line number accepted"
    assert not test3_file.delete(6), "delete() : Positive Invalid line number accepted"
    assert test3_file.delete(-5), "delete() : Negative valid line number not accepted"
    assert str(test3_file.textlist) == "22\n33\n44\n55\n", "delete() : Not working as expected"

    print("Test Passed")

def search_test():
    """
    Tests search() function. I modified search() to return string of lines found for testing
    :precondition: all txt files must be described as below
    :complexity: O(1), because all txt files must be fixed
    """
    def search(testfile, word):
        """
        Searches every line that contains the word
        :param word: Query word to search
        :complexity: O(N^2)
        """
        word = word.lower()  # Converts to lowercase, to make case insensitive
        string_toprint = ""  # Temporary string that stores the found lines

        for index in range(len(testfile.textlist)):
            line_nosp = ""  # a string that will store the text line without special characters
            line = testfile.textlist[index].lower()  # Converts the textline in list to lowercase as well
            for char in line:  # for every character in line,
                if char.isalnum() or char == " ":  # If char is alphabet or numeric, or whitespace,
                    line_nosp += char  # add it to line_nosp
            if word in line_nosp:  # If the query word is found at a line
                line_num = index +1  # Because line starts from 1
                string_toprint += str(line_num) + " "
        return string_toprint

    ### Test file ###
    test1_file = Editor()  # test_search1.txt has [A, FOUND, A, A, found]
    test1_file.textlist = test1_file.arraylist_readfile("test_search1.txt")

    test2_file = Editor()  # test_search2.txt has [A, FOUN, A, foun, FoUnD]
    test2_file.textlist = test2_file.arraylist_readfile("test_search2.txt")

    test3_file = Editor()  # test3.txt has [A, foun, F'oun,d, F..ound, A, f/o,und] (to check ignoring special characters)
    test3_file.textlist = test3_file.arraylist_readfile("test_search3.txt")

    ### Test ###
    print("\n===Testing search===")
    assert search(test1_file, "FOUND") == "2 5 ", "search() : test1, Not working as expected"
    assert search(test1_file, "A") == "1 3 4 ", "search() : test1, Not working as expected"
    assert search(test1_file, "Hello") == "", "search() : test1, Non-existing word found"

    assert search(test2_file, "Found") == "5 ", "search() : test2, Not working as expected"
    assert search(test2_file, "Foun") == "2 4 5 ", "search() : test2, Not working as expected"
    assert search(test2_file, "fou") == "2 4 5 ", "search() : test2, Not working as expected"

    assert search(test3_file, "FoUn") == "2 3 4 6 ", "search() : test3, Not working as expected"
    assert search(test3_file, "found") == "3 4 6 ", "search() : test3, Not working as expected"

    print("Test Passed")



def test_functions():
    """
    Main function for testing
    :complexity: O(1)
    """
    convert_line_toindex_test()
    insert_test()
    read_test()
    write_test()
    print_test()
    delete_test()
    search_test()
    """
    1. I did not Include test for arraylist_readfile() because I used the function from Task4, so the test is included in task4_test
    2. Also, I did not test quit() because it only uses the python built-in function exit().
    3. All of them has no precondition on Array_Based_List functions because it can be tested in Task2_test, so I assumed that they work properly
    """



test_functions()