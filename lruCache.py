# Time Complexity :
# 1. get : O(1)
# 2. put : O(1)
# Space Complexity : 
# O(N), where N is the number of elements in the cache
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach
# 1. we will use a doubly linked list to keep track of the order of elements in the cache.
# 2. The head of the list will represent the most recently used element, and the tail will represent the least recently used element.
# 3. We will also use a hash map to store the key-value pairs for quick access, since searching is involved when we need to get or put an element in the cache.
# 4. When we get an element, we will move it to the head of the list to mark it as recently used.
# 5. When we put an element, we will check if it already exists in the cache. If it does, we will update its value and move it to the head of the list.
# 6. If it doesn't exist and the cache is full, we will remove the least recently used element (the tail of the list) and add the new element to the head of the list.
# 7. If it doesn't exist and the cache is not full, we will simply add the new element to the head of the list.

# Definition for a doubly linked list node
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:
    # Initialize the LRUCache with a given capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Create a dummy head and tail node to represent the start and end of the list
        # The head node will point to the most recently used element
        self.head = ListNode(-1, -1)
        # The tail node will point to the least recently used element
        self.tail = ListNode(-1, -1)
        # Link the head and tail nodes to each other
        self.head.next = self.tail
        self.tail.prev = self.head
        # Create a hash map to store the key-value pairs
        # The key will be the cache key and the value will be the corresponding ListNode
        self.hashMap = {}

    # Helper function to add a node to the head of the list
    # This function will be called when we get or put an element in the cache
    def addToHead(self, node):
        # Add the node to the head of the list
        # The new node's next pointer will point to the current head's next node
        node.next = self.head.next
        # The new node's previous pointer will point to the head node
        node.prev = self.head
        # # The head node's next pointer will point to the new node
        self.head.next = node
        # The current head's next node's previous pointer will point to the new node
        node.next.prev = node

    # Helper function to remove a node from the list
    # This function will be called when we need to remove the least recently used element or when we get an element
    def removeNode(self, node):
        # Remove the node from the list
        # The current node's next node's previous pointer will point to the current node's previous node
        node.next.prev = node.prev
        # The current node's previous node's next pointer will point to the current node's next node
        node.prev.next = node.next
        # Set the current node's next and previous pointers to None
        # This is optional, but it helps with garbage collection and makes it clear that the node is no longer part of the list
        node.next = None
        node.prev = None

    # Get the value of the key if it exists in the cache
    def get(self, key: int) -> int:
        # Check if the key exists in the hash map
        if key in self.hashMap:
            # If it exists, get the corresponding node from the hash map
            node = self.hashMap[key]
            # Remove the node from its current position in the list
            self.removeNode(node)
            # Add the node to the head of the list to mark it as recently used
            self.addToHead(node)
            # Return the value of the node
            return node.val
        # If the key doesn't exist, return -1
        return -1

    # Put a key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        # Check if the key already exists in the hash map
        if key in self.hashMap:
            # If it exists, get the corresponding node from the hash map
            node = self.hashMap[key]
            # Remove the node from its current position in the list
            self.removeNode(node)
            # Update the value of the node
            node.val = value
            # Add the node to the head of the list to mark it as recently used
            self.addToHead(node)
        # If the key doesn't exist, we need to add a new node
        else:
            # Check if the cache is full
            # If it is full, remove the least recently used element (the tail's previous node)
            if len(self.hashMap) == self.capacity:
                # Get the least recently used node (the tail's previous node)
                oldNode = self.tail.prev
                # Remove the least recently used node from the linked list
                self.removeNode(oldNode)
                # Remove the least recently used node from the hash map
                del self.hashMap[oldNode.key]
            # Create a new node with the given key and value
            newNode = ListNode(key, value)
            # Add the new node to the head of the list to mark it as recently used
            self.addToHead(newNode)
            # Add the new node to the hash map
            self.hashMap[key] = newNode