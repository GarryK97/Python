"""
The Node that will be used in Trie of SequenceDatabase
"""
class SequenceDatabaseNode:
    def __init__(self, size=5): # Size = 5 because only A,B,C,D + terminal character
        """
        Initializes the class variables
        :param size: The range of possible alphabets + terminal character. (e.g. all small letter alphabets = 26 + 1 )
        :Complexity: Best Time: O(1), Worst Time: O(size), Aux Space: O(size)
        """
        self.link = [None for x in range(size)]  # Needs 'size' spaces
        self.frequency = 0  # Stores the frequency of the Sequence inserted
        self.sequence = ""  # Stores the sequence
        self.most_sequence_node = None  # Stores the Node of the Sequence with highest frequency


"""
The Sequence Database class that will store the DNA sequence A-D
"""
class SequenceDatabase:
    def __init__(self):
        """
        Initializes the root
        :Complexity: Best Time: O(1), Worst Time: O(1), Aux Space: O(1)
        """
        self.root = SequenceDatabaseNode()

    def addSequence(self, key):
        """
        Adds the DNA sequence (key) to the database Trie, using recursive function.
        :param key: DNA sequence to add
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)^2), Aux Space: O(N)
        """
        current = self.root # Initialize the current as root
        self.addSequence_recur_aux(current, 0, key)
        self.root_data_addition(key)

    def addSequence_recur_aux(self, current, idx, sequence):
        """
        Recursive funtion to add the sequence (key) in the Trie database.
        :param current: The current node to begin
        :param idx: The index of a character that is currently inserted into Trie
        :param sequence: The sequence to add
        :return: The Node of the sequence with the highest frequency at a prefix
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)^2), Aux Space: O(len(key))
        """
        # Base case
        if len(sequence) == idx:
            # when I gone through all of my letters
            # If path exist, ( = already a sequence exist)
            if current.link[0] is not None:
                current = current.link[0]
            # If path does not exist ( = new sequence inserting)
            else:
                current.link[0] = SequenceDatabaseNode()
                current = current.link[0]
            current.frequency += 1  # Increment the frequency at the leaf node
            current.sequence = sequence  # Stores the Sequence
            return current  # Returns the leaf node
        else:
            # calculate index ($, A, B, ...)
            index = ord(sequence[idx]) - ord("A") + 1  # + terminal string
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path does not exist
            else:
                current.link[index] = SequenceDatabaseNode()
                current = current.link[index]

            new_most_node = self.addSequence_recur_aux(current, idx+1, sequence)  # Recursion. The letter that is already added will be removed.

            if current.most_sequence_node is None:
                # If a node does not have any stored node, (may due to new sequence addition)
                current.most_sequence_node = new_most_node  # Stores the optimal node, which is delivered from the child node
            else:
                # If a node already has an optimal node, Need to compare the new node to replace optimal node
                if new_most_node.frequency > current.most_sequence_node.frequency:
                    # If the new node frequency is higher,
                    current.most_sequence_node = new_most_node  # Replace it
                elif new_most_node.frequency == current.most_sequence_node.frequency and new_most_node.sequence < current.most_sequence_node.sequence:
                    # else if the frequency of the both nodes are the same, compare the alphabetical order
                    current.most_sequence_node = new_most_node

            return current.most_sequence_node   # Returns the optimal node (will be used in parent node during recursion)

    def root_data_addition(self, key):
        """
        This function is to Store the sequence with the highest frequency at the root node
        This Will be used in addSequence() function
        :param key: An existing sequence which is already in the database.
        :Complexity: Best Time: O(1), Worst Time: O(len(S)), Aux Space: O(1)
                                        S = The Shorter Stored optimal sequence between root node and child node
        """
        root_node = self.root
        first_char = key[0]  # Take the first character only because the child node has the optimal node already.

        index = ord(first_char) - ord("A") + 1  # + terminal string
        child_node = root_node.link[index]

        if root_node.most_sequence_node is None:
            # If root node does not have any stored optimal node,
            root_node.most_sequence_node = child_node.most_sequence_node
        else:
            # If the root node already has an optimal node, Need to compare the new node to replace optimal node
            if child_node.most_sequence_node.frequency > root_node.most_sequence_node.frequency:
                # If the child's optimal node.frequency is higher,
                root_node.most_sequence_node = child_node.most_sequence_node  # Replace it
            elif child_node.most_sequence_node.frequency == root_node.most_sequence_node.frequency and child_node.most_sequence_node.sequence < root_node.most_sequence_node.sequence:
                # else if the frequency of the both nodes are the same, compare the alphabetical order
                root_node.most_sequence_node = child_node.most_sequence_node

    def query(self, query_key):
        """
        Search for the stored sequence that matches the query_key as a prefix
        :param query_key: a string to query (possible empty)
        :return: The sequence with the highest frequency. If multiple sequences have the same frequency, return the lexicographically least sequence.
        :Complexity: Best Time: O(len(query_key)), Worst Time: O(len(query_key)), Aux Space: O(1)
        """
        current = self.root

        if not len(query_key) == 0:  # = If the query_key is not empty,
            for char in query_key:
                index = ord(char) - ord("A") + 1
                if current.link[index] is None:  # = If there is no matching sequence,
                    return None
                else:
                    current = current.link[index]   # Go to child node

        return current.most_sequence_node.sequence


# -------------------------- Q2


"""
The Node that will be used in Trie in SuffixTrie and PrefixTrie
"""
class TrieNode:
    def __init__(self, size=5): # Size = 5 because only A,B,C,D + terminal character
        """
        Initializes the class variables
        :param size: The range of possible alphabets + terminal character. (e.g. all small letter alphabets = 26 + 1 )
        :Complexity: Best Time: O(1), Worst Time: O(size), Aux Space: O(size)
        """
        self.link = [None for x in range(size)]  # Needs 'size' spaces
        self.start_index = []  # Will store the index where a suffix or prefix starts.(e.g. put "ABCD", A = 0, B = 1, C = 2 ...)


"""
The Suffix Trie which stores all suffixes of the genome
"""
class SuffixTrie:
    def __init__(self, genome):
        """
        Initializes the root and construct a Suffix Trie of 'genome'
        :Complexity: Best Time: O(len(genome)^2), Worst Time: O(len(genome)^2), Aux Space: O(len(genome))
        """
        self.root = TrieNode()
        self.genome = genome

        for i in range(len(genome)+1):  # +1 to store empty string
            self.insert(i, self.root)   # insert every suffix (e.g. "ABCD" -> "ABCD, "BCD", "CD" ...)

    def insert(self, idx, current):
        """
        Inserts the key(suffix) in the Trie, using recursion insert_recur_aux()
        :param idx: The start index of a suffix (e.g. "ABCD", suffix "BCD" -> idx = 1)
        :param current: The Starting node to insert
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)), Aux Space: O(len(key))
        """
        self.insert_recur_aux(current, idx)

    def insert_recur_aux(self, current, idx):
        """
        Recursive function to insert the suffix(key) into Trie.
        :param current: The starting node to insert
        :param idx: The index of a character that is currently inserted into Trie
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)), Aux Space: O(len(key))
        """
        # Base case
        if len(self.genome) <= idx:
            # when I gone through all of my letters
            current.link[0] = TrieNode()
            return
        else:
            # calculate index ($, A, B, ...)
            index = ord(self.genome[idx]) - ord("A") + 1  # + terminal string
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path does not exist
            else:
                # create a new node
                current.link[index] = TrieNode()
                current = current.link[index]
            current.start_index.append(idx)  # Append the start_index in the node's data
            self.insert_recur_aux(current, idx+1)  # Recursion. Removes the letter that is already added and move the start_index.


"""
The Prefix Trie which stores all prefixes of the genome
"""
class PrefixTrie:
    def __init__(self, genome):
        """
        Initializes the root and construct a Prefix Trie of 'genome'
        :Complexity: Best Time: O(len(genome)^2), Worst Time: O(len(genome)^2), Aux Space: O(len(genome))
        """
        self.root = TrieNode()
        self.genome = genome

        for i in reversed(range(len(genome))):
            self.insert(i, self.root)    # # insert every prefixes

    def insert(self, idx, current):
        """
        Inserts the key(prefix) in the Trie, using recursion insert_recur_aux()
        :param idx: The end index of the prefix (e.g. "ABCD", prefix "ABC" -> idx = 2)
        :param current: The Starting node to insert
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)), Aux Space: O(len(key))
        """
        self.insert_recur_aux(current, idx)

    def insert_recur_aux(self, current, idx):
        """
        Recursive function to insert the prefix(key) into Trie.
        :param current: The starting node to insert
        :param idx: The index of a character that is currently inserted into Trie
        :Complexity: Best Time: O(len(key)), Worst Time: O(len(key)), Aux Space: O(len(key))
        """
        # Base case
        if idx < 0:
            # when I gone through all of my letters
            current.link[0] = TrieNode()
            return
        else:
            # calculate index ($, A, B, ...)
            index = ord(self.genome[idx]) - ord("A") + 1  # - ord(a) + terminal string
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path does not exist
            else:
                # create a new node
                current.link[index] = TrieNode()
                current = current.link[index]
            current.start_index.append(idx)  # Append the start_index in the node's data
            self.insert_recur_aux(current, idx-1)  # Recursion. Removes the letter that is already added and move the start_index.

"""
The OrfFinder class to store ORF and to find the DNA that matches a particular sequence.
"""
class OrfFinder:
    def __init__(self, genome):
        """
        Stores the genome and construct Tries that store all the suffixes and prefixes.
        :param genome: The genome to store
        :Complexity: Best Time: O(len(genome)^2), Worst Time: O(len(genome)^2), Aux Space: O(len(genome))
        """
        self.genome = genome
        self.suffix_trie = SuffixTrie(genome)
        self.prefix_trie = PrefixTrie(genome)

    def find_start_index(self, start_str):
        """
        Finds all the starting index that matches the pattern 'start_str'. (e.g. "ABCBC" | str = "BCBC" -> [1,3] )
        :param start_str: The prefix to search
        :return: List that stores all the starting index that matches 'start_str'
        :Complexity: Best Time: O(1), Worst Time: O(len(S) + len(A)), Aux Space: O(len(A))
                                            S = start_str , A = suffix_array
        """
        current = self.suffix_trie.root
        suffix_array = []
        found = False   # False = No matching suffixes, True = At least one matching suffix exist

        for char in start_str:
            # calculate index ($, A, B, ...)
            index = ord(char) - ord("A") + 1  # + terminal string
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
                found = True
            # If path does not exist, = No matching suffix
            else:
                return suffix_array

        if found:   # = if there is at least one matching suffix
            current = self.suffix_trie.root
            for char in start_str:
                index = ord(char) - ord("A") + 1  # + terminal string
                current = current.link[index]
            suffix_array += current.start_index  # Transfer the data from the node of last character, = end index of the suffix

            # As suffix_array has the end indexes of the suffix, we need to minus, to get the start index
            for i in range(len(suffix_array)):
                suffix_array[i] -= len(start_str)-1

        return suffix_array

    def find_end_index(self, end_str):
        """
        Finds all the end index that matches the pattern 'end_str'. (e.g. "ABCBC" | str = "BC" -> [4,2] )
        :param end_str: The suffix to search
        :return: List that stores all the end index that matches 'end_str'
        :Complexity: Best Time: O(1), Worst Time: O(len(S) + len(A)), Aux Space: O(len(A))
                                            S = end_str , A = prefix_array
        """
        current = self.prefix_trie.root
        end_str = end_str[::-1]  # Reverse the string as PrefixTrie stored the prefixes in reversed order
        found = False  # False = No matching prefixes, True = At least one matching prefix exist
        prefix_array = []

        for char in end_str:
            # calculate index ($, A, B, ...)
            index = ord(char) - ord("A") + 1  # + terminal string
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
                found = True
            # If path does not exist, = No matching prefix
            else:
                return prefix_array

        if found:   # = if there is at least one matching prefix
            current = self.prefix_trie.root
            for char in end_str:
                index = ord(char) - ord("A") + 1  # + terminal string
                current = current.link[index]
            prefix_array += current.start_index  # Transfer the data from the node of first character, = start index of prefix

            # As prefix_array has the start indexes of the prefix, we need to plus, to get the end index
            for i in range(len(prefix_array)):
                prefix_array[i] += len(end_str)-1

        return prefix_array

    def find(self, start_str, end_str):
        """
        Finds the list of sub-sequences that matches the prefix(start_str) and suffix(end_str)
        :param start_str: the prefix to search
        :param end_str: the suffix to search
        :return: List of sub-sequences
        :Complexity: Best Time: O(1), Worst Time: O(len(P)*len(S) + len(I)*U), Aux Space: O(len(P) + len(S))
                                    P = prefix_index List , I = sub_genome_indexes List
                                    S = suffix_index List , U = Total number of characters in sub_genome_list
        """
        prefix_index = self.find_start_index(start_str)  # Stores all start index of matching suffix
        suffix_index = self.find_end_index(end_str)  # Stores all end index of matching prefix
        sub_genome_indexes = []  # Stores (start_index, end_index) of valid sub-genomes
        sub_genome_list = []  # Stores all the sub-genomes, = output

        for start_index in prefix_index:
            for end_index in suffix_index:
                if (end_index + 1 - start_index) >= len(start_str) + len(end_str):  # To prevent invalid sub-genomes (e.g. prefix and suffix overlaps)
                    sub_genome_indexes.append((start_index, end_index))

        for indexes in sub_genome_indexes:
            start_index = indexes[0]
            end_index = indexes[1]
            sub_genome_list.append(self.genome[start_index:end_index + 1])  # String Slice takes 'end_index - start_index' times

        return sub_genome_list
