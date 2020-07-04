class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()