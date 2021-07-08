def counting_Sort(a_list, base, power):
    """
    Implementation of counting sort according to the nth digit numbers for radix sort.
    :param a_list: a list to sort according to nth digit numbers. (n = power + 1)
    :param base: base which is used in this function (e.g. hexadecimal, binary)
    :param power: exponent
    :return: the sorted list according to the nth digit numbers.
    :complexity: Time: O(N+b), Auxiliary space = O(N+b)
                 N = size of a_list, b = base
                 -Best Time: O(N+b)
                 -Worst Time: O(N+b)
    """
    counts = [0 for x in range(base)]  # counts[] saves the frequency
    for item in a_list:
        num_ofdigit = (item // (base**power)) % base  # Num_ofdigit = the nth digit number
        counts[num_ofdigit] += 1    # +1 count[the number] = +1 the frequnecy

    # Converting the counts to rank array (position array)
    # Counts at each position = current + previous counts (cumultaive counts)
    # counts[number]-1 will give the position for the number
    for i in range(1, base):
        counts[i] += counts[i - 1]

    # This prevents the original list being changed when sorting.
    output = [0 for x in range(len(a_list))]
    # Going reverse as my counts (rank array) stores cumulative counts
    for item in reversed(a_list):
        num_ofdigit = (item // (base**power)) % base
        output[counts[num_ofdigit] - 1] = item  # -1, as count has 1 more index than the given list.
        counts[num_ofdigit] -= 1    # -1 to go to next position when the same digit number appears.

    return output

def radix_Sort(alist, base):
    """
    alist will be sorted by looping through counting_Sort().
    :param alist: a list to sort
    :param base: base which is used in this function (e.g. hexadecimal, binary)
    :return: a sorted list
    :complexity: Time: O(k(N+b)), Auxiliary space: O(N+b)
                N = size of alist, b = base, k = maximum number of digits
                -Best Time: O(N+b)
                -Worst Time: O(k(N+b))
    """
    if len(alist) == 0:  # If empty, return the original to prevent errors
       return alist

    max_num = max(alist)    # Necessary to terminate loop below
    output = alist.copy()   # Making a copy not to make changes the original list
    power = 0
    while max_num // (base**power) > 0:  # = Loop until it reaches maximum digit
        output = counting_Sort(output, base, power)     # Continue to call counting_Sort() until all digits are sorted
        power += 1  # Digit position = power + 1  e.g.)if power = 2, 3rd digits are being sorted
    return output


def best_interval(transaction, t):
    """
    Finds the best interval that contains most transaction(element) in the list "transaction", using t as range.
    This function uses radix_Sort().
    :param transaction: a list that contains transaction
    :param t: range of interval (e.g. t = 5, range = (0,5) inclusive )
    :return: a tuple (best_t, best_count), best_t = minimal t value & best_count = the number of item in best_t range.
    :complexity: Time:O(k(N)) , Auxiliary space = O(N)
                N = size of transaction, k = maximum number of bits in transaction
                -Best Time: O(N)
                -Worst Time: O(k(N))
    """
    sorted_transaction = radix_Sort(transaction, 2)     # calling radix sort with base 2
    best_t = 0  # Stores the minimal start point that has best counts
    best_count = 0  # stores the highest count in range t

    # Explanation of this loop :
    # It goes through all the items in the transaction until start_index reaches the limit
    # end_index starts from the end and goes through the items from the behind.
    # After some loop, when start item and end item is in range t, it will count the items in the range
    # if the count of current range is bigger than the best count saved, it will replace the best count
    if len(sorted_transaction) != 0:   # if transaction list is not empty, (to avoid errors)
        start_index = 0
        while start_index < len(sorted_transaction):    # Until start_index reaches the limit
            end_index = len(sorted_transaction)-1   # end_index start from the behind
            start_item = sorted_transaction[start_index]
            end_item = sorted_transaction[end_index]
            while end_item - start_item > t and end_index > 0:  # = search for values until end_index reaches limit
                end_index -= 1
                end_item = sorted_transaction[end_index]

            current_count = len(sorted_transaction[start_index:end_index+1])    # Get the count within the found range
            if current_count > best_count:  # Replacing best count
                best_count = current_count
                if end_item - t > 0:    # To prevent best_t becomes negative,
                    best_t = end_item - t
            start_index += 1    # Continue to search for next

    return (best_t, best_count)


# Task 2 -----------------------------------------

def counting_Sort_Length(a_list, base, power):
    """
    Implementation of counting sort according to the nth digit numbers for radix sort.
    :param a_list: a list to sort according to nth digit numbers. (n = power + 1)
    :param base: base which is used in this function (e.g. hexadecimal, binary)
    :param power: exponent
    :return: the sorted list according to the nth digit numbers.
    :complexity: Time = O(N+b) , Auxiliary space = O(N+b)
                N = size of a_list, b = base
                -Best Time: O(N+b)
                -Worst Time: O(N+b)
    """
    counts = [0 for x in range(base)]  # counts[] saves the frequency
    for item in a_list:
        len_item = len(item)
        num_ofdigit = (len_item // (base**power)) % base  # Num_ofdigit = the nth digit number
        counts[num_ofdigit] += 1    # +1 count[the number] = +1 the frequnecy

    # Converting the counts to rank array (position array)
    # Counts at each position = current + previous counts (cumultaive counts)
    # counts[number]-1 will give the position for the number
    for i in range(1, base):
        counts[i] += counts[i - 1]

    # This prevents the original list being mixed-up when sorting.
    output = [0 for x in range(len(a_list))]
    # Going reverse as my counts (rank array) stores cumulative counts
    for item in reversed(a_list):
        len_item = len(item)
        num_ofdigit = (len_item // (base**power)) % base
        output[counts[num_ofdigit] - 1] = item  # -1, as count has 1 more index than the given list.
        counts[num_ofdigit] -= 1    # -1 to go to next position when the same digit number appears.

    return output


def radix_Sort_Length(alist, base):
    """
    alist will be sorted according to the length of strings by looping through counting_Sort_Length().
    It requires a base parameter to perform because the length can be very large.
    :param alist: a list to sort
    :param base: base which is used in this function (e.g. hexadecimal, binary)
    :return: a sorted list according to the length of strings.
    :complexity: Time: O(k(N+b)), Auxiliary space: O(N+b)
                N = size of alist, b = base, k = maximum number of digits
                -Best Time: O(N+b)
                -Worst Time: O(k(N+b))
    """
    if len(alist) == 0:  # If empty, return the original to prevent errors
       return alist

    max_len = 0
    for word in alist:
        if len(word) > max_len:
            max_len = len(word)
    output = alist.copy()   # Making a copy not to make changes the original list
    power = 0
    while max_len // (base**power) > 0:  # Continue to call counting_Sort() until all digits are sorted
        output = counting_Sort_Length(output, base, power)
        power += 1  # Digit position = power + 1  e.g.)if power = 2, 3rd digits are being sorted
    return output


def counting_Sort_Word(a_string):
    """
    Implementation of counting sort for a string. It will return the sorted string in alphabetical order.
    :param a_string: a string to sort
    :return: the sorted string in alphabetical order
    :complexity: Time = O(L) , Auxiliary space = O(L)
                    L = Length of the a_string
                -Best Time: O(L)
                -Worst Time: O(L)
    """
    counts = [0 for x in range(26)]     # 26 because there are 26 alphabets
    for letter in a_string:
        value = ord(letter)-97  # Num_ofdigit = the nth digit number. -97 as minimum base is ord("a) = 97
        counts[value] += 1    # +1 count[the number] = saving the frequnecy

    # Converting the counts to rank array (position array)
    # Counts at each position = current + previous counts (cumultaive counts)
    # counts[number]-1 will give the position for the number
    for i in range(1, 26):
        counts[i] += counts[i - 1]

    # This prevents the original list being changed when sorting.
    output = [0 for x in range(len(a_string))]
    # Going reverse as my counts (rank array) stores cumulative counts
    for letter in reversed(a_string):
        value = ord(letter)-97
        output[counts[value] - 1] = letter  # -1, as count has 1 more index than the given list.
        counts[value] -= 1    # -1 to go to next position when the same digit number appears.

    # Joins the characters into one string
    out_str = ""
    for letter in output:
        out_str += letter

    return out_str


def counting_Sort_Stringlist(a_list, col):
    """
    Counting sort for a list contains strings.
    :param a_list: a list with strings
    :param col: column that will be sorted ( will be used inside radix_Sort_Stringlist() )
    :return: a sorted array, which is sorted by column.
    :complexity: Time: O(N), Auxiliary space = O(N)
                 N = size of a_list
                 -Best Time: O(N)
                 -Worst Time: O(N)
    """
    base = 26+1   # base 26 and +1, as counts must store dummy data when column > length
    counts = [0 for x in range(base)]   # Initializing counts which will store frequency
    min_base = ord("a")-1   # -1 so that the dummy can be stored
    for word in a_list:
        if col < len(word): # If the word is within column range
            value = ord(word[col])-min_base  # Gets the ASCII value and minus the base "a"
            counts[value] += 1  # +1 count[the number] = saving the frequnecy
        else:
            counts[0] += 1  # if word is out of range, store the dummy

    # Converting the counts to rank array (position array)
    # Counts at each position = current + previous counts (cumultaive counts)
    # counts[number]-1 will give the position for the number
    for i in range(1, base):
        counts[i] += counts[i - 1]

    # This prevents the original list being mixed-up when sorting.
    output = [0 for x in range(len(a_list))]
    # Going reverse as my counts (rank array) stores cumulative counts
    for word in reversed(a_list):
        if col < len(word):
            value = ord(word[col])-min_base
            output[counts[value] - 1] = word  # -1, as count has 1 more index than the given list.
            counts[value] -= 1    # -1 to go to next position when the same digit number appears.
        else:   # Same process for words that are out of range.
            output[counts[0] - 1] = word
            counts[0] -= 1

    return output

def radix_Sort_Stringlist(a_list):
    """
    Radix sort, which uses count_Sort_Stringlist. This function sorts a list of strings.
    :param a_list: a list to sort
    :return: a new sorted list of a_list
    :complexity: Time = O(NM) , Auxiliary space = O(N)
                N = size of a_list, M = the number of characters of a longest string.
                -Best Time: O(N)
                -Worst Time: O(NM)
    """
    if len(a_list) == 0:    # If empty, return empty list to prevent possible errors.
        return []

    # Getting the max length of a word in the list
    max_len = 0
    for word in a_list:
        if len(word) > max_len:
            max_len = len(word)

    output = a_list.copy()  # Creating a copy not to make changes to the original list.

    col = max_len-1
    while col >= 0:     # Looping through every column and sorts the list column by column
        output = counting_Sort_Stringlist(output, col)
        col -= 1

    return output


def words_with_anagrams(list1, list2):
    """
    This function finds the anagram of a list1 string, inside list2. All anagram found will be stored in list format.
    :param list1: a list of strings
    :param list2: a list of strings, which is used to find anagrams inside list2 for a list1 string.
    :return: a list of list1 strings, which anagram is found inside list2.
    :complexity: Time = O(L1*S2(M1+M2)) , Auxiliary space = O(L1 + L2)
                L1, L2 = number of elements in List1, List2  /   M1, M2 = number of characters of the longest string
                S2 = list2 strings which has the same length as a string in list1 (L1)

            -Best Time : O(L1M1+L2M2)
            -Worst Time: O(L1*S2(M1+M2))
    """
    # Sorting the list by alphabetical order for efficient comparison.
    # Comparing two sorted lists will have less time cost, rather than comparing raw lists.
    list1_sorted = radix_Sort_Stringlist(list1)
    list2_sorted = radix_Sort_Stringlist(list2)

    # Resort the sorted list, so that it can be grouped by the length of strings.
    # It is because anagram can only be found with strings that have the same length.
    list1_sorted = radix_Sort_Length(list1_sorted, 2)
    list2_sorted = radix_Sort_Length(list2_sorted, 2)

    output = []     # Output which will be returned
    pointer = 0     # pointer will store the start position of strings with the same length.
    for item1 in list1_sorted:
        for item2 in list2_sorted[pointer:]:    # All strings below the pointer will be ignored
            if len(item1) == len(item2):    # If same length, then compare the words.
                if counting_Sort_Word(item1) == counting_Sort_Word(item2):
                    output.append(item1)
                    break   # Stop comparing list1 item, once anagram found.
            elif len(item1) > len(item2):
                pointer += 1    # = Need to move pointer to next length, so that the next loop can be more efficient
            else:   # = No anagram found
                break   # Stop comparing list1 item, as no anagram exists.

    return output




