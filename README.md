# AlgorithmsPractice
Repository oriented on most common used algorithms. Practice and implementation will be written in Python. 

List of algorithms:<br/>
1. HashMaps<br/>
2. Recursion<br/>
3. DFS & BFS<br/>
4. Binary Search<br/>
5. Sliding Window<br/>
6. Heaps

---
## Recursion
Links: 
* https://www.youtube.com/watch?v=KEEKn7Me-ms&ab_channel=HackerRank
* https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/

A recursive algorithm is an algorithm which calls itself with "smaller (or simpler)" input values, and which obtains the result for the current input by applying simple operations to the returned value for the smaller (or simpler) input.<br/>
Properties of Recursion:
* Performing the same operations multiple times with different inputs.
* In every step, we try smaller inputs to make the problem smaller.
* Base condition is needed to stop the recursion otherwise infinite loop will occur.

Stack Overflow Error - if the base case is not reached or not define

|Recursion | Iteration|
|----------|----------|
|Used in functions | Used in loops
|Every recursive call needs extra space in the stack memory.|Every iteration does not require any extra space.|
|Smaller code size.|Larger code sizes|

## DFS & BFS
### DFS
* https://www.youtube.com/watch?v=Urx87-NMm6c
* https://www.youtube.com/watch?v=iaBEKo5sM7w&t=57s&ab_channel=GoGATEIIT
* https://www.youtube.com/watch?v=by93qH4ACxo&ab_channel=BroCode
* https://favtutor.com/blogs/depth-first-search-python

Algorithm for searching a graph (depth = vertical before horizontal)
The applications of using the DFS algorithm are given as follows:
* DFS algorithm can be used to implement the topological sorting.
* It can be used to find the paths between two vertices.
* It can also be used to detect cycles in the graph.
* DFS algorithm is also used for one solution puzzles.
* DFS is used to determine if a graph is bipartite or not.

What do we do once have to solve a maze? We tend to take a route, keep going until we discover a dead end. When touching the dead end, we again come back and keep coming back till we see a path we didn't attempt before. Take that new route. Once more keep going until we discover a dead end. Take a come back again… This is exactly how Depth-First Search works.


### BFS
* https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
* https://www.youtube.com/watch?v=HZ5YTanv5QE&ab_channel=MichaelSambol
* https://www.simplilearn.com/tutorials/data-structure-tutorial/bfs-algorithm
* https://www.youtube.com/watch?v=0u78hx-66Xk&pp=ygUSYmZzIGFsZ29yaXRobSBnZWVr&ab_channel=GeeksforGeeks


Algorithm for searching a graph (breadth = broad/wide)
The breadth-first search or BFS algorithm is used to search a tree or graph data structure for a node that meets a set of criteria. It begins at the root of the tree or graph and investigates all nodes at the current depth level before moving on to nodes at the next depth level. 
With it you can resolve problems like, i.e.: finding the shortest path between two vertices a and b is determined by the number of edges.

Application Of Breadth-First Search Algorithm:
* For Unweighted Graphs, You Must Use the Shortest Path and Minimum Spacing Tree:<br/>
The shortest path in an unweighted graph is the one with the fewest edges. You always reach a vertex from a given source using the fewest amount of edges when utilizing breadth-first. In unweighted graphs, any spanning tree is the Minimum Spanning Tree, and you can identify a spanning tree using either depth or breadth-first traversal.
* Crawlers in Search Engine:<br/>
Crawlers create indexes based on breadth-first. The goal is to start at the original page and follow all of the links there, then repeat. Crawlers can also employ Depth First Traversal. However, the benefit of breadth-first traversal is that the depth or layers of the created tree can be limited.
* Crawlers in Search Engine:<br/>
Crawlers create indexes based on breadth-first. The goal is to start at the original page and follow all of the links there, then repeat. Crawlers can also employ Depth First Traversal. However, the benefit of breadth-first traversal is that the depth or layers of the created tree can be limited.

---
## Binary Search
Links: 
* https://www.programiz.com/dsa/binary-search
* https://www.geeksforgeeks.org/binary-search/
Binary Search is a searching algorithm for finding an element's position in a sorted array.In this approach, the element is always searched in the middle of a portion of an array.<br/>
To apply Binary Search algorithm:
* The data structure must be sorted.
* Access to any element of the data structure takes constant time.

*Advantages of Binary Search:*
* Binary search is faster than linear search, especially for large arrays.
* More efficient than other searching algorithms with a similar time complexity, such as interpolation search or exponential search.
* Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud.

*Drawbacks of Binary Search:*
* The array should be sorted.
* Binary search requires that the data structure being searched be stored in contiguous memory locations. 
* Binary search requires that the elements of the array be comparable, meaning that they must be able to be ordered.

---
## Sliding Window
Links: 
* https://medium.com/geekculture/implement-a-sliding-window-using-python-31d1481842a7
* https://www.geeksforgeeks.org/window-sliding-technique/

Window Sliding Technique is a computational technique that aims to reduce the use of nested loops and replace it with a single loop, thereby reducing the time complexity.
A sliding window is a subset of a data structure at a given point of time. The window size decides the number of elements in the subset.<br/>
The basic idea behind the sliding window technique is to transform two nested loops into a single loop.

The sliding window technique can also be implemented using generators.Generators usually store the state of the execution and resume when called the next time. The *yield* keyword inside a function determines that the function is a generator.

Use cases:
* Calculate substrings of specific length from a longer string
* Calculate the sum of consecutive n numbers in a list where n will be the window size
* Take hashmap or dictionary to count specific array input and uphold on increasing the window towards right using an outer loop
* Take one inside a loop to reduce the window side by sliding towards the right. This loop will be very short
* Store the current maximum or minimum window size or count based on the problem statement
---
## Heaps
Links: 
* https://www.youtube.com/watch?v=0wPlzMU-k00&pp=ygURaGVhcCBpbiAzIG1pbnV0ZXM%3D
* https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

heap == data structure to manage information
Heap data structure is mainly used to represent a priority queue.<br/>
**Note** that the *heapq* module in Python provides functions for performing heap operations on lists in-place, without creating a separate data structure for the heap. The *heapq* module is efficient and easy to use, making it a popular choice for implementing priority queues and other data structures in Python.

- binary heap
- nearly complete binary tree
  - every parent node, at most, can have only 2 children
  - must be complete tree. It must be filled from left to right and every level must be full, with the exception of the last level not needing to be full

Use cases:

**Priority queues:** Heaps can be used to implement priority queues, where each element has a priority associated with it and elements with higher priorities are given priority over elements with lower priorities.

**Sorting:** Heapsort is a comparison-based sorting algorithm that uses a heap data structure to sort a list of elements. It has a time complexity of O(n*log(n)).

**Graph algorithms:** Heaps are often used in graph algorithms, such as Dijkstra’s shortest path algorithm and the A* search algorithm, to efficiently determine the next element to be processed.

**Median maintenance:** Heaps can be used to maintain the median of a stream of numbers by using a max-heap to store the smaller half of the numbers and a min-heap to store the larger half.

**Resource allocation:** Heaps can be used to efficiently allocate resources in a system, such as memory blocks or CPU time, by assigning a priority to each resource and processing requests in order of priority.

**Selection algorithms:** Heaps can be used in selection algorithms, such as the quickselect algorithm, to efficiently find the k-th smallest element in a list.

Types: 
* max-heap
  * every parent's key must be greater than its children nodes
* min-heap
  * every parent's key must be smaller than its children nodes

**Advantages of using a heap queue (or heapq) in Python:**
* Efficient: A heap queue is a highly efficient data structure for managing priority queues and heaps in Python. It provides logarithmic time complexity for many operations, making it a popular choice for many applications.
* Space-efficient: Heap queues are space-efficient, as they store elements in an array-based representation, minimizing the overhead associated with node-based data structures like linked lists.
* Easy to use: Heap queues in Python are easy to use, with a simple and intuitive API that makes it easy to perform basic operations like inserting, deleting, and retrieving elements from the heap.
* Flexible: Heap queues in Python can be used to implement various data structures like priority queues, heaps, and binary trees, making them a versatile tool for many applications.

**Disadvantages of using a heap queue (or heapq) in Python:**
* Limited functionality: Heap queues are primarily designed for managing priority queues and heaps, and may not be suitable for more complex data structures and algorithms.
* No random access: Heap queues do not support random access to elements, making it difficult to access elements in the middle of the heap or modify elements that are not at the top of the heap.
* No sorting: Heap queues do not support sorting, so if you need to sort elements in a specific order, you will need to use a different data structure or algorithm.
* Not thread-safe: Heap queues are not thread-safe, meaning that they may not be suitable for use in multi-threaded applications where data synchronization is critical.
