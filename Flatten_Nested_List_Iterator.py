# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # The line `self.stack = [(nestedList, 0)]` initializes the stack with a tuple containing the
        # given `nestedList` and an index of 0. This represents the current position in the nested
        # list that the iterator is pointing to.
        self.stack = [(nestedList, 0)]

    def next(self):
        """
        :rtype: int
        """

        self.hasNext()
        # `nestedList, index = self.stack[-1]` is unpacking the tuple at the top of the stack into two
        # variables `nestedList` and `index`. This allows us to access the current nested list and the
        # current index within that nested list.
        nestedList, index = self.stack[-1]
        self.stack[-1] = (nestedList, index + 1)
        return nestedList[index].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # This code block is checking if the current nested list in the stack has been fully traversed. If the
        # index is equal to the length of the nested list, it means that all elements in the nested list have
        # been visited, so the current nested list is popped from the stack.
        while self.stack:
            # `nestedList, index = self.stack[-1]` is unpacking the tuple at the top of the stack into
            # two variables `nestedList` and `index`. This allows us to access the current nested list
            # and the current index within that nested list.
            nestedList, index = self.stack[-1]
            if index == len(nestedList):
                self.stack.pop()
            # This code block is checking if the current element in the nested list is an integer or a nested
            # list. If it is an integer, it returns True, indicating that there is a next element. If it is a
            # nested list, it updates the stack to point to the next element in the current nested list and pushes
            # the nested list onto the stack to be traversed later. This allows the iterator to handle nested
            # lists and iterate through all the integers in the nested structure.
            else:
                element = nestedList[index]
                if element.isInteger():
                    return True
                self.stack[-1] = (nestedList, index + 1)
                self.stack.append((element.getList(), 0))
        return False

        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())