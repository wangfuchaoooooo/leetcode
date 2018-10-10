class MinStack0:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack is None:
            return 'ERROR'
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return 'ERROR'
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return 'ERROR'
        return min(self.stack)


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """

        popItem = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
            return popItem

        if popItem == self.min:
            self.min = self.stack[0]
            for i in self.stack:
                if i < self.min:
                    self.min = i
        return popItem

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())

    print(minStack.getMin())
