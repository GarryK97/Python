from Task3 import HashTable


def threefiles_test():
    # Function used to make the prime_mult table for Task2
    ### Testing the 3 files given ###

    # Open files and add them into lists
    f = open("english_small.txt", 'rt', encoding='UTF8')
    eng_small = []
    for line in f:
        line = line.strip()
        eng_small.append(line)
    f.close()

    f = open("english_large.txt", 'rt', encoding='UTF8')
    eng_large = []
    for line in f:
        line = line.strip()
        eng_large.append(line)
    f.close()

    f = open("french.txt", 'rt', encoding='UTF8')
    french = []
    for line in f:
        line = line.strip()
        french.append(line)
    f.close()

    ### Testing Start ###
    value = "test"  # A temporary(placeholder) value for testing
    n = 1
    for text_file in [eng_small, eng_large, french]:
        print("\n---Testing file " + str(n))  # file 1, 2, 3 = eng_small, eng_large, french
        n += 1
        hashtable = HashTable(300151, 1064)  # 300151 and 1064 are the best combinations found in Task2
        for key in text_file:
            hashtable[key] = value

        print("\nMultiplier Value = " + str(1064))
        print("Number of items = " + str(hashtable.count))
        print("Initial Table size = " + str(300151))
        print("Changed Table size = " + str(hashtable.table_size))
        print("Load = " + str(hashtable.load))
        print("Total Collisions = " + str(hashtable.collision_count))
        print("Total Probe Length = " + str(hashtable.probe_count))
        print("Average Probe Length = " + str(hashtable.avg_probe_len))


threefiles_test()


"""
--- Comparison between Linear Probing and Quadratic Probing ---
 
Collisions : 

In two text files, english_small.txt and french.txt, Quadratic probing showed less collisions.
Especially, the collision count almost decreased by half in french.txt, while english_small.txt had very small differences.
In printed results, you can see that the table size is doubled in french.txt and the load is decreased by half as well.
So, I can conclude that dynamic hashing (dynamic table size) is significantly helpful in avoiding collisions of hash values.
However, when french.txt is tested by using dynamic hashing, the running time was definitely higher than the Task2 Linear Probing.
It is because my dynamic hashing() function must copy all the existing items and rehash all the items again to put them into
a newly created array.
In english_large.txt, collisions increased 6 times, but can be considered as the same collisions with Linear probing because
it is an extremely small difference, compared to the item size of english_large.txt (194433).

Probe Length :

In all the text files, the probe length is significantly reduced, compared to the Linear Probing.
In english_small.txt, probe length is reduced by 1,120 (6.5% reduced).
In english_large.txt, probe length is reduced by 66,005 (33% reduced).
In french.txt, probe length is reduced by 209,638 (80% reduced).

Even though english_small.txt and english_large.txt had very small differences in collision count, probe length of
both text files had huge differences.
In french.txt, the probe length also significantly reduced as well. So, I found that dynamic hashing is also helpful
in reducing search time of hash table.

Conclusion :
Quadratic probing is important in reducing both collisions and probe length.
"""