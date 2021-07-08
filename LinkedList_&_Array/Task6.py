from Task3 import LinkedList


class Editor:
    def __init__(self):
        """
        Initializing object's varaible
        """
        self.textlist = LinkedList()  # Initializing list from Task2

    def linkedlist_readfile(self, filename):
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

    def convert_line_toindex(self, line_num):
        """
        Converts line number to list index, because line number starts from 1, but list index starts from 0
        But, with negative numbers, both numbers are the same
        :param line_num: Line number to check
        :return: List index, or None (if line_num is not valid)
        :precondition: nested is_linenum_inbound() function must have no error
        :complexity: O(1)
        """
        def is_linenum_inbound(line_num):
            """
            Checks whether the line number is valid or not (means, line number should be greater than 0 or less than 0)
            :param line_num: Line number to check
            :return: True, if Line number valid. Else, False
            :complexity: O(1)
            """
            if line_num == 0:  # Because line start from 1 or -1
                return False
            elif line_num > 0:
                if line_num > len(self.textlist):  # If line_num greater than maximum line_num
                    return False
            elif line_num < 0:
                if line_num < -len(self.textlist):  # If line_num smaller than minimum line_num
                    return False
            return True  # If all okay, return True

        if is_linenum_inbound(line_num):  # Checks if the line_num is valid
            if line_num > 0:  # If line_num is positive,
                return line_num-1  # -1 because index starts from 0
            else:
                return line_num  # If negative, return the same line_num
        else:
            return None  # Return None means the line number is not valid, which means conversion failed

    def insert(self, line_num):
        """
        Inserts a user's text input into the line number (num)
        :param line_num: Line number to insert
        :return: True, if insert successful. False, if failed
        :precondition: convert_line_toindex() must have no error
        """
        if line_num == len(self.textlist) + 1:  # If user wants to insert a text at the last,
            user_text = input("Write a text : ")
            self.textlist.append(user_text)  # use append function to add the text
            return True

        else:  # Else, in normal case,
            index = self.convert_line_toindex(line_num)  # Convert line_num to index
            if index is not None:  # If conversion successful,
                user_text = input("Write a text : ")  # Gets user's text input
                self.textlist.insert(index, user_text)
                return True
            else:  # index == None means conversion failed (not valid line_num),
                return False

    def read(self, filename):
        """
        Reads a text file and put texts into elements, line by line
        :param filename: Filename to read
        :return: True, if read successful, False if failed
        :precondition: linkedlist_readfile() must have no error
        :complexity: O(N), including linkedlist_readfile()
        """
        try:
            self.textlist = self.linkedlist_readfile(filename)  # textlist now has the texts of the file
            return True
        except FileNotFoundError:  # If file is not found, print error message
            return False

    def write(self, filename):
        """
        Writes texts in textlist to a file. If the file does not exist, creates a new file and write.
        :param filename: Filename to write
        :return: True, if write successful. False, if failed
        :complexity: O(N)
        """
        try:  # Should not have any error at all
            file = open(filename, "w+")  # w+ means, try to open 'filename', if no file, creates a new text file.
            for text in self.textlist:
                file.write(text + "\n")  # To write the text at separated lines
            file.close()
            return True
        except:  # In case of any unexpected errors,
            return False

    def print(self, line_num1, line_num2):
        """
        Prints the lines between line_num1 and line_num2
        :param line_num1: Starting line
        :param line_num2: Ending line
        :return: True, if print successful. False, if failed
        :precondition: convert_line_toindex() must have no error
        :complexity: Average Case : O(N), depends on line_num1 and line_num2
        """
        index1 = self.convert_line_toindex(line_num1)  # Converts line number to index
        index2 = self.convert_line_toindex(line_num2)
        if index1 is not None and index2 is not None and index1 < index2: # If both conversion successful and index1 < index2
            string_toprint = ""
            for index in range(index1, index2+1):  # index2 +1, because for loop is exclusive
                string_toprint += self.textlist[index] + "\n"
            print(string_toprint)
            return True
        else:  # If conversion failed, or index1 > index2
            return False

    def delete(self, line_num=None):
        """
        Deletes a specific line, if no line_num given, resets the self.textlist
        :param line_num: Line number to delete
        :return: True, if delete successful. False, if failed
        :precondition: convert_line_toindex() must have no error
        :complexity: O(1)
        """
        if line_num is None:  # If no number given,
            self.textlist = LinkedList()  # Reset
            return True

        else:  # If any number is given
            index = self.convert_line_toindex(line_num)
            if index is not None:  # If conversion successful, (valid line number)
                self.textlist.delete(index)
                return True
            else:  # index == None, means line_num is not valid
                return False

    def search(self, word):
        """
        Searches every line that contains the word
        :param word: Query word to search
        :complexity: O(N^2)
        """
        word = word.lower()  # Converts to lowercase, to make case insensitive
        string_toprint = ""  # Temporary string that stores the found lines

        for index in range(len(self.textlist)):
            line_nosp = ""  # a string that will store the text line without special characters
            line = self.textlist[index].lower()  # Converts the textline in list to lowercase as well
            for char in line:  # for every character in line,
                if char.isalnum() or char == " ":  # If char is alphabet or numeric, or whitespace,
                    line_nosp += char  # add it to line_nosp
            if word in line_nosp:  # If the query word is found at a line
                line_num = index +1  # Because line starts from 1
                string_toprint += str(line_num) + " "

        if string_toprint == "":
            print("No line contains the word")
        else:
            print("Found at Line number : " + string_toprint)  # Prints the result

    def quit(self):
        """
        Ends the program
        :complexity: O(1)
        """
        exit()  # Python built-in function to end program


    def menu_start(self):
        """
        Editor's Main function to start it and print menu
        :precondition: all the functions defined in Editor class must work properly
        :complexity: Best Case : O(1), Worst Case : O(N)
        """
        ### Printing Menu ###
        print("=== Editor Menu ===\n")
        print("1. insert num")
        print("2. read filename")
        print("3. write filename")
        print("4. print num1 num2")
        print("5. delete num")
        print("6. search word")
        print("7. quit")


        while True:  # Will loop forever until the user quits.
            ### Get user input ###
            menu_input = input("\nEnter a command: ").lower()  # To make it case insensitive
            menu_input = menu_input.split(" ")
            command = menu_input[0]
            first_input = menu_input[1]

            ### Call function ###
            if command == "insert":
                try:
                    line_num = int(first_input)
                    if not self.insert(line_num):  # If insert failed,
                        print("??")
                except ValueError:  # If first_input cannot be converted into int type
                    print("??")

            elif command == "read":
                filename = first_input
                if not self.read(filename):  # If read failed,
                    print("??")

            elif command == "write":
                filename = first_input
                if not self.write(filename):  # Write should have no error, but in case of any errors
                    print("??")

            elif command == "print":
                try:
                    line_num1 = int(first_input)
                    line_num2 = int(menu_input[2])
                    if not self.print(line_num1, line_num2):  # If print failed,
                        print("??")
                except ValueError:  # If first_input or second input cannot be converted to int type
                    print("??")
                except IndexError:  # If there's no second input, will cause IndexError
                    print("??")

            elif command == "delete":
                try:
                    line_num = int(first_input)
                    if not self.delete(line_num):  # If delete failed,
                        return False
                except ValueError:
                    print("??")

            elif command == "search":
                query_word = first_input
                self.search(query_word)

            elif command == "quit":
                self.quit()

            else:
                print("Error : Please enter a valid command")