from Task3 import HashTable


def read_file_removesp(file_name):
    """
    Read a text file and convert it to a list of words without any special characters.
    :param file_name: File to read
    :return: the list of words
    """
    f = open(file_name, 'rt', encoding='UTF8')
    file_list = []
    for line in f:
        line = line.strip()  # Remove whitespaces
        line = line.split(" ")  # Split by words
        for i in range(len(line)):
            word_nosp = ""  # String that will store word with no special character
            line[i] = line[i].lower()  # Lower the word to make search easy
            for char in line[i]:  # for each character in word,
                if char.isalpha():  # if the character is not special character (if it is alphabet),
                    word_nosp += char  # Add it to word_nosp
            if word_nosp != "":  # To prevent adding white spaces and already existing words
                file_list.append(word_nosp)  # Append the word with no special character
    f.close()
    return file_list


book1 = read_file_removesp("Book1.txt")
book2 = read_file_removesp("Book2.txt")
book3 = read_file_removesp("Book3.txt")

book_hashtable = HashTable(399989, 1091)

# Making a hash table
for books in [book1, book2, book3]:
    for word in books:
        try:
            count = book_hashtable[word]  # if the word exists in hash table, count will store the value of it
            book_hashtable[word] = count + 1  # + 1 count
        except KeyError:
            book_hashtable[word] = 1  # If the word does not exist in hash table, it means a new word needs to be added

# Making a non-duplicate words list
words_list = []
for books in [book1, book2, book3]:
    for word in books:
        if word not in words_list:
            words_list.append(word)

# Finding Maximum
max_count = 0
max_word = ""
for word in words_list:
    if book_hashtable[word] > max_count:  # if word count > current maximum word count,
        max_count = book_hashtable[word]  # Change to new max count and word
        max_word = word

# Finding common, uncommon, rare words
common_words = []
uncommon_words = []
rare_words = []

for word in words_list:  # Zipf's law in simple python code
    if book_hashtable[word] > (max_count / 100):
        common_words.append(word)
    elif book_hashtable[word] > (max_count / 1000):
        uncommon_words.append(word)
    else:
        rare_words.append(word)

print("Number of common words : " + str(len(common_words)))   # Prints the result
print("Number of uncommon words : " + str(len(uncommon_words)))
print("Number of rare words : " + str(len(rare_words)))
