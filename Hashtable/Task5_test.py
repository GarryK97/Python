##########  Task5 codes copied and modified   ########################
from Task3 import HashTable

book1 = []
book2 = []
book3 = []
for _ in range(10000):  # In total, a count = 30000  (Should be maximum word, and common words)
    book1.append("a")
    book2.append("a")
    book3.append("a")

for _ in range(101):  # In total, b count = 303  (Should be common words)
    book1.append("b")
    book2.append("b")
    book3.append("b")

for _ in range(20):  # In total, c count = 60  (Should be uncommon words)
    book1.append("c")
    book2.append("c")
    book3.append("c")

for _ in range(3):  # In total, d count = 9  (Should be rare words)
    book1.append("d")
    book2.append("d")
    book3.append("d")

####### Below codes are not changed #############
book_hashtable = HashTable(399989, 1091)

# Making a hash table
for books in [book1, book2, book3]:
    for word in books:
        try:
            count = book_hashtable[word]  # if the word exists in hash table, count will store the value of it
            book_hashtable[word] = count + 1  # + 1 count
        except KeyError:
            book_hashtable[word] = 1  # If the word does not exist in hash table, it means new word need to be added

# Making a non-duplicate words list
words_list = []
for books in [book1, book2, book3]:
    for word in books:
        if word not in words_list:
            words_list.append(word)

# Find Maximum
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

###############  Test Codes  ######################

assert book_hashtable["a"] == 30000 and book_hashtable["b"] == 303 and book_hashtable["c"] == 60 and book_hashtable["d"] == 9, "Word count(Hashtable value) is not working as expected"

assert max_word == "a" and max_count == 30000, "Max_word and Max_count not working as expected"

assert common_words == ["a", "b"] and uncommon_words == ["c"] and rare_words == ["d"], "Common, uncommon, rare words list not working as expected"
