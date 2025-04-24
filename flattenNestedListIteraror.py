# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# Time Complexity : O(1) for hasNext and next
# Every call to next() will make a call to advance(), which will iterate through the nested list, and might take O(N) time in the worst case to get an integer, where N is the depth of the nested list.
# However, this is amortized over multiple calls to next(), so the average time complexity for each call to next() is O(1).
# Space Complexity : O(1) for the stack, which is used to keep track of the nested list.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# 1. We will use a stack to keep track of the nested list.
# The stack will be used to store the iterators of the nested list.
# 2. We will start by pushing the iterator of the outermost list onto the stack.
# 3. The advance() function will be called to get the next integer.
# 4. In the advance() function, we will pop the top iterator from the stack and get the next element.
# 5. If the next element is an integer, we will set it as the nextEl.
# 6. If the next element is a nested list, we will push its iterator onto the stack.
# 7. The hasNext() function will check if there is a next element by checking if nextEl is not None.

class NestedIterator:
    # Initialize the iterator with the nested list
    # The constructor takes a nested list as input and initializes the stack
    def __init__(self, nestedList):
        # Initialize the stack with the iterator of the nested list
        self.stack = []
        self.stack.append(iter(nestedList))
        # Call the advance() function to get the first integer
        self.advance()

    # The advance() function is used to get the next integer from the nested list
    def advance(self):
        # Set the nextEl to None
        self.nextEl = None
        # Iterate through the stack until we find an integer or the stack is empty
        while self.stack:
            # Get the next element from the top iterator in the stack
            tmp = next(self.stack[-1], None)
            # If the iterator is exhausted, pop it from the stack
            if tmp == None:
                self.stack.pop()
            # If the iterator is not exhausted, check if it is an integer or a nested list
            else:
                # If it is an integer, set it as the nextEl
                if tmp.isInteger():
                    self.nextEl = tmp.getInteger()
                    # Break the loop as we have found the next integer
                    break
                # If it is a nested list, push its iterator onto the stack
                else:
                    self.stack.append(iter(tmp.getList()))

    # The next() function returns the next integer from the nested list
    # It calls the advance() function to get the next integer
    def next(self) -> int:
        # Store the current nextEl in a temporary variable
        tmp = self.nextEl
        # Call the advance() function to get the next integer
        # This will update the nextEl to the next integer
        self.advance()
        # Return the current nextEl
        return tmp
        
    # The hasNext() function checks if there is a next integer in the nested list
    def hasNext(self) -> bool:
        # If we have a next element, it means there is a next integer
        return self.nextEl != None