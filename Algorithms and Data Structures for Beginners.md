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

- Let us overcome the issue of not knowing the final required length of the array before the program's completion.
- In some languages, we wrap a static array with special functions to keep track of its size (i.e., the number of elements it currently contains) and capacity (i.e., the number of elements it can currently store) as an implementation of a dynamic array.
- We resize the array using a Doubling Strategy; that is, we double the capacity whenever the array is fully filled.
- The time complexity of this doubling comes out to around $\mathcal{O}(1)$, as we need to double the array less and less; with each successive doubling, we get more free slots.
- The time complexity of the standard operations is the same as that of static arrays.

### Stacks

- Stacks are a special type of contiguous data structure where we can only add, remove, and view the last element. There is a direct analogy between this structure and a stack of real-world objects.
- All operations are $O(1)$. We refer to these operations as *pushing* to the stack, *popping* from the stack, and *peeking* from the stack to denote adding, deleting, and viewing elements.
- Under the hood, this would be implemented with a dynamic array.

## Linked Lists

### Singly Linked Lists

- Composed of `ListNode`s, which hold the value and a pointer to the next element.
- Because they point to the next element, we can place them in discontinuous places in memory and can easily append and remove elements.
- Getting the last element has the following pseudocode: we continuously traverse the `ListNode`s via pointers until we reach the tail, whose next pointer is `None`:

```py
current = head
while current is not None:
  current = current.next
```

- We can add an index flag within this loop to get the $\text{i}^{\text{th}}$ element.
- Appending to the list would have the following: we change the value of the tail's next pointer to the new element and then make the tail the new last element:

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

- Doubly linked lists are, as the name suggests, they contain pointers to both the next *and* previous nodes.
- This allows us to make insertions and deletions at the ends of the linked list efficiently.
- As with singly linked lists, inserting and deleting middle elements is also $O(1)$.
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

- We can summarize the time complexities of the doubly-linked list in the following table:

| Operation            | Time Complexity | Notes                                               |
| -------------------- | --------------- | --------------------------------------------------- |
| Accessing an element | $O(n)$          |                                                     |
| Finding an element   | $O(n)$          |                                                     |
| Adding elements | $O(1)$          | This assumes we have a pointer directly to the end. Adding elements to the middle is usually just $O(n)$. |
| Deleting elements    | $O(1)$          | This assumes we have a pointer to the desired node. |

### Queues

- Queues are another fundamental data structure. They operate by the principle of First In, First Out (FIFO).

- An example is when people line up, the person who lined up first, gets served first.

- Generally implemented as a Linked List under the hood.

- There are two operations we perform on queues: enqueue and dequeue

- ```python
  def enqueue(self, val):
      newNode = ListNode(val)
  
      if self.right:
          self.right.next = newNode
          self.right = self.right.next
      else:
          self.left = self.right = newNode
          
  def dequeue(self):
      if not self.left:
          return None
      
      val = self.left.val
      self.left = self.left.next
      if not self.left:
          self.right = None
      return val
  ```

- The time complexity for both operations is $\mathcal{O}(1)$.

## Factorial

- Recursion is when a function calls itself with a different input.

- A recursive function is composed of 2 parts: the base case and the recursive case(s). 

  - When there are multiple recursive cases, it's called multi-branch; otherwise, it's called single-branch.

- The simplest example is the factorial function: $n!=n\cdot(n-1)\cdot(n-2)\dots3\cdot2\cdot\cdot1$.

- ```python
  def factorial(n):
      if n == 1:  # Base Case
          return 1
      else: # Recursive case
          return n * factorial(n - 1)
  ```

- Since there will be $n$ recursive calls, the time complexity of this function is in $\mathcal{O}(n)$. Additionally, since we need to maintain $n$ stack frames, the space complexity is also in $\mathcal{O}(n)$.

- We can often convert recursive problems to iterative ones, but some problems lend themselves well to recursive approaches (Trees, Graphs, etc.)

## Fibonacci Sequence

- ```python
  def fibonacci(n):
      if n <= 1:  # Base Case
          return n
      else:  # Recursive Case
          return fibonacci(n - 1) + fibonacci(n - 2)
  ```

- Since we have 2 function calls with reach recursion, for a given $n$, we have $2^{n+1}-1$ total function calls which gives us a time complexity of $\mathcal{O}(2^n)$.