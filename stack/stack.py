class Stack:
    def __init__(self):
        self.stack = ['5', '6', '7']

    def isEmpty(self):
        return len(self.stack)==0

    def isFull(self):
        return len(self.stack)>0

    def push(self):
        self.stack.append(['1', '2', '3'])
        return True

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]