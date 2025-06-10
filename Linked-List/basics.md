# 📓 Data Structures Notes

## 📘 Topic 1: What is a Linked List?

A **Linked List** is a linear data structure where elements are stored in **nodes**, and each node points to the next one in the sequence. Unlike arrays or normal lists, the elements are not stored in contiguous memory locations.

Each node typically contains:
- The **data** (the actual value)
- A **reference** or pointer to the **next** node in the list

There are different types of linked lists:
- **Singly Linked List** – each node points only to the next node.
- **Doubly Linked List** – each node points to both the next and the previous node.
- **Circular Linked List** – the last node links back to the first node.

### 📌 Example (Conceptual)
Imagine a train:
- Each **carriage** is like a **node**
- The **link** between carriages is like the **pointer**
- The **train** is the whole linked list

### 🆚 Linked List vs Normal List (Array)

| Feature                  | Linked List                          | Normal List (Array)              |
|--------------------------|--------------------------------------|----------------------------------|
| **Memory Allocation**    | Dynamic (non-contiguous)             | Static or dynamic (contiguous)   |
| **Insert/Delete**        | Efficient (especially at start/middle) | Can be costly (requires shifting) |
| **Access Time**          | Linear (must traverse nodes)         | Constant (direct access via index) |
| **Size**                 | Grows as needed                      | May require resizing or copying  |
| **Pointer Usage**        | Uses extra memory for pointers       | No pointers used                 |

### 📝 Summary

- Linked lists are useful when frequent insertion/deletion is needed.
- Arrays/lists are better when you need fast random access.
- Choosing between them depends on the specific problem and constraints.

---

### Types of LinkedList

There are three types of Linked list
- Singly linked list 
- Doubly linked list
- Circular linked list

---

Now that we have covered the basics move to **singly_linked_list.py**
