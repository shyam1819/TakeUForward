class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minEle = None
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.minEle is None:
            self.minEle = val
            self.stack.append(val)
            return
        elif val<self.minEle:
            self.stack.append((2*val) - self.minEle)
            self.minEle = val
            return

        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if self.stack==[]:
            self.minEle = None
            return
        if val<self.minEle: 
            self.minEle = ((2*self.minEle)-val)
        

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        return top if top>self.minEle else self.minEle
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minEle
        
