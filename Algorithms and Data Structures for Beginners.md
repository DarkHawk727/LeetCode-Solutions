# Algorithms and Data Structures for Beginners

## Arrays

### RAM

- What is a data structure? A way data is arranged in memory.
- RAM is measured in bytes; a byte is 8 bits.
- Integers often occupy 4 bytes (4bytes x 8 bits per byte = 32 bits)
- An address and a value get associated with each thing stored in the array.
- RAM is a contiguous section of memory

### Static Arrays

- Some lower-level languages have fixed-size arrays.
- The following table can sum up operations:

| Operation | Time Complexity | Notes                                                        |
| --------- | --------------- | ------------------------------------------------------------ |
| Reading   | $O(1)$          |                                                              |
| Inserting | $O(n)$          | Worst-case: If the element is to be inserted at the beginning. |
| Deleting  | $O(n)$          | Worst-case: If the element is to be deleted from the beginning. |

### Dynamic Arrays

- Let us get over the issue of not knowing the final required length of the array before completion of the program.
- In some languages, we wrap a static array with special functions to keep track of the size (how many elements the array currently has) and capacity (how many elements the array can currently store) as an implementation of a dynamic array.
- We resize the array using a Doubling Strategy; that is, we double the capacity whenever we fully fill up the array.
- The time complexity of this doubling comes out to around $O(1)$ as we need to double the array less and less as each successive time we double, we get more free slots.
- The time complexity of the usual operations is the same as in static arrays.

### Stacks

- Stacks are a special type of contiguous data structure where we can only add, remove, and view the last element. There is a direct analogy between this structure an a stack of real-world objects.
- All operations are $O(1)$. We call them *pushing to the stack*, *popping from the stack* and *peeking from the stack* to denote adding, deleting, and viewing elements.
- Under the hood, this would be implemented with a dynamic array.

## Linked Lists

### Singly Linked Lists

- Composed of `ListNode`s, which hold the value and a pointer to the next element.
- Because they point to the next element, we can place them in discontinuous places in memory and can easily append and remove elements.
- Getting the last element has the following pseudocode, we continuously traverse the listnodes via pointers until we reach the tail, whose next pointer is `None`:

```py
current = head
while current is not None:
  current = current.next
```

- We can add an index flag within this loop to get the $\text{i}^{\text{th}}$ element.
- Appending to the list would have the following, we change the value of the tail's next pointer to the new element and then make the tail the new last element:

```py
tail.next = nodeToBeAdded
tail = nodeToBeAdded
```

- Their operations are summed up in the following table:

| Operation            | Time Complexity | Notes                                               |
| -------------------- | --------------- | --------------------------------------------------- |
| Accessing an element | $O(n)$          |                                                     |
| Finding an element   | $O(n)$          |                                                     |
| Appending to the end | $O(1)$          | This assumes we have a pointer directly to the end. |
| Deleting elements    | $O(1)$          | This assumes we have a pointer to the desired node. |

### Doubly Linked Lists

- Doubly linked lists are as the name suggests, they contain pointers to both the next *and* previous nodes.
- This allows us to make insertions and deletions at the ends of the linked list efficiently.
- As with singly linked lists, inserting and deleting the middle elements is also $O(1)$.
- Adding to the end has the following pseudocode:

```py
tail.next = nodeToBeAdded
nodeToBeAdded.prev = tail
tail = tail.next
```

- Similarly, deleting from the end would look like:

```py
newLastNode = tail.prev
newLastNode.next = null
tail = newLastNode
```

- We can sume the time complexities of the doubly-linked list in the following table:

| Operation            | Time Complexity | Notes                                               |
| -------------------- | --------------- | --------------------------------------------------- |
| Accessing an element | $O(n)$          |                                                     |
| Finding an element   | $O(n)$          |                                                     |
| Adding elements | $O(1)$          | This assumes we have a pointer directly to the end. Adding elements to the middle is usually just $O(n)$. |
| Deleting elements    | $O(1)$          | This assumes we have a pointer to the desired node. |


### Queues

