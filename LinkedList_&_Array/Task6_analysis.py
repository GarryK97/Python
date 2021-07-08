"""
=== Comparison between Array List and Linked List ===
"""

"""
Task5 : Array List
=== Strength === 
1. Items (Elements) of the list can be directly accessed via list index
2. Therefore, getting an element from Array List has the lowest time complexity, which is O(1)

=== Weakness ===
1. Takes too much spaces (memory) because memory must be occupied in advance to append or insert items in the list
2. Even if the most of the items are removed, the occupied memory is not decreasing efficiently.
( e.g. num_items = 1280, size = 1280 --> Remove 1200 items --> num_items = 80, size = 640)
Likewise, although most of the items are removed, size only decreased by half and left 560 spaces, which is very inefficient
3. All the Items must be pushed in front or behind after append, insert, remove and delete, to fill up the empty spaces
"""

"""
Task6 : Linked List
=== Strength ===
1. Linked List only occupies the memory for existing items (Efficient memory usage)
2. append, insert, remove and delete is very flexible and easy, compared to Array List

=== Weakness ===
1. Linked List has much higher time complexity than Array List, which is O(N) as Linked List must go through
all the previous index to get one index item.
2. Linked List takes more memory per item, as Array List only requires a space for the item,
however, Linked List must have more space to store the pointer (.next link)
"""

"""
=== Conclusion ===
I will choose Array List implementation for the best performance, to deal with a large size text files.

The reasons : 
1. If the text file becomes significantly huge, getting a text line from Linked List would be highly time-consuming.
In my view, users do not want to wait for 10 seconds to get a single text line.
2. In large text files, four modification functions (append, insert, remove, delete) of Linked List will be extremely time-consuming.
Especially, append() will take a lot of time, as it has to go through all the items in the Linked list, while Array List
simply use index to add the item.
3. I think that the memory wastage of array list is not a big problem, 
because, computers nowadays have incredible memory spaces and have enough spaces to store multiple of large text files.
4. sort in Linked List is extremely inefficient as it has to go through O(N) loops every time to get an index item and
to compare it with another index item. If the text file has a large size, there will be a significant time difference


However, if I am sure that the text file will not be large, (e.g. less than 500 text lines)
I will choose Linked List implementation for the performance, because the time complexity is not a
big problem in small-sized text files. If there is no big difference in time-consumption, Linked List should be used
to prevent memory wastage of Array List.
"""