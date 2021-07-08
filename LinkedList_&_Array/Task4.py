from Task2 import Array_Based_List
from Task3 import LinkedList


def arraylist_readfile(filename):
    """
    Reads a file and make a Array_Based_List class object
    :param filename: name of the file (string)
    :return: created Array_Based_List object
    :complexity: O(N)
    """
    user_file = open(filename)

    array_list = Array_Based_List()
    for line in user_file:
        line = line.strip()  # Removes whitespace and change text
        array_list.append(line)  # append to the list by line
    user_file.close()
    return array_list


def linkedlist_readfile(filename):
    """
    Reads a file and make a LinkedList class object
    :param filename: name of the file (string)
    :return: created LinkedList object
    :complexity: O(N)
    """
    user_file = open(filename)

    linked_list = LinkedList()
    for line in user_file:
        line = line.strip()  # Removes whitespace and change text
        linked_list.append(line)  # append to the list by line
    user_file.close()
    return linked_list