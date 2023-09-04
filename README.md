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

Uses: 
* heapsort
* priority queues

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
