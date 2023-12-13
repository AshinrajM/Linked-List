A **Linked List** is a linear data structure, in which the elements are not stored at contiguous memory locations.
The elements in a linked list are linked using pointers. linked list consists of nodes where each node contains
a data field and a reference(link) to the next node in the list.


<p align="left"><b>Types of Linked List</b></p>

<p align="left">1.Singly Linked List </p>

<p align="left">2.Doubly Linked List </p>

<p align="left">3.Circular Linked List </p>

<p align="left">4.Circular Doubly Linked List </p>

<p align="left">5.Header Linked List </p>


__Linked Lists are most commonly used for:__

=>Linked Lists are mostly used because of their effective insertion and deletion. 

=>Insertion and deletion in the linked list are very effective and take less time complexity as compared to
  the array data structure. 
  
=>This data structure is simple and can be also used to implement a stack, queues, and other abstract data structures.  


__Applications of Linked Lists in real world:__

=>The list of songs in the music player are linked to the previous and next songs. 

=>In a web browser, previous and next web page URLs are linked through the previous and next buttons.

=>In image viewer, the previous and next images are linked with the help of the previous and next buttons.

__Advantages of Linked Lists:__

=>**Dynamic size:** Linked lists do not have a fixed size, so you can add or remove elements as needed, without having to worry 
  about the size of the list.This makes linked lists a great choice when you need to work with a collection of items whose size 
  can change dynamically.
  
=>**Efficient Insertion and Deletion:** Inserting or deleting elements in a linked list is fast and efficient, 
  as you only need to modify the reference of the next node, which is an O(1) operation.

=>**Memory Efficiency:** Linked lists use only as much memory as they need, so they are more efficient with memory
  compared to arrays, which have a fixed size and can waste memory if not all elements are used.

=>**Easy to Implement:** Linked lists are relatively simple to implement and understand compared to other 
  data structures like trees and graphs.

=>**Flexibility:** Linked lists can be used to implement various abstract data types, such as stacks, queues,
  and associative arrays.

=>**Easy to navigate:** Linked lists can be easily traversed, making it easier to find specific elements or perform
  operations on the list.

__Disadvantages of Linked Lists:__

=>**Slow Access Time:** Accessing elements in a linked list can be slow, as you need to traverse the linked list to 
  find the element you are looking for, which is an O(n) operation. This makes linked lists a poor choice for situations
  where you need to access elements quickly.

=>**Pointers:** Linked lists use pointers to reference the next node, which can make them more complex to understand and
  use compared to arrays. This complexity can make linked lists more difficult to debug and maintain.

=>**Higher overhead:** Linked lists have a higher overhead compared to arrays, as each node in a linked list requires 
  extra memory to store the reference to the next node.

=>**Cache Inefficiency:** Linked lists are cache-inefficient because the memory is not contiguous. This means that when you 
  traverse a linked list, you are not likely to get the data you need in the cache, leading to cache misses and slow performance.

=>**Extra memory required:** Linked lists require an extra pointer for each node, which takes up extra memory. 
  This can be a problem when you are working with large data sets, as the extra memory required for the pointers can quickly add up.


