from Task2 import HashTable


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
    test_multiplier = [1064, 1091]  # Non-prime, Prime
    test_size = [300000, 300151]  # 300151 is prime number, (obtained by using prime calculator)
    value = "test"  # A temporary(placeholder) value for testing

    n = 1
    for text_file in [eng_small, eng_large, french]:
        print("\n---Testing file " + str(n))  # file 1, 2, 3 = eng_small, eng_large, french
        n += 1
        for tablesize in test_size:
            for multiplier in test_multiplier:
                hashtable = HashTable(tablesize, multiplier)  # Making a hashtable for each multiplier and table size
                for key in text_file:
                    hashtable[key] = value

                print("\nMultiplier Value = " + str(multiplier))
                print("Number of items = " + str(hashtable.count))
                print("Table size = " + str(tablesize))
                print("Load = " + str(hashtable.load))
                print("Total Collisions = " + str(hashtable.collision_count))
                print("Total Probe Length = " + str(hashtable.probe_count))
                print("Average Probe Length = " + str(hashtable.avg_probe_len))


def collision_probe_test():
    # Used lecture examples for testing (because it's very time consuming to calculate all the hash values and find collisions)
    value = "Test"  # A temporary value (placeholder) for testing
    test_keys = ["Aho", "Kruse", "Standish", "Horowitz", "Langsam", "Sedgewick", "Knuth"]

    a_hashtable = HashTable(7, 3)
    for key in test_keys:
        a_hashtable[key] = value
    assert a_hashtable.collision_count == 3, "collision_probe_test() : Collision count something wrong"
    assert a_hashtable.probe_count == 5, "collision_probe_test() : Probe count something wrong"

    b_hashtable = HashTable(128, 1024)
    for key in test_keys:
        b_hashtable[key] = value
    assert b_hashtable.collision_count == 1, "collision_probe_test() : Collision count something wrong"
    assert b_hashtable.probe_count == 1, "collision_probe_test() : Probe count something wrong"

    c_hashtable = HashTable(101, 31)
    for key in test_keys:
        c_hashtable[key] = value
    assert c_hashtable.collision_count == 0, "collision_probe_test() : Collision count something wrong"
    assert c_hashtable.probe_count == 0, "collision_probe_test() : Probe count something wrong"




### Did not include test for probe_count as it is difficult to track the correct probe length.
### Did not include test for other functions as they are imported from Task1

threefiles_test()
collision_probe_test()



