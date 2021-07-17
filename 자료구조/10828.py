class stack:
    stacklist=[]
    def __init__(self):
        self.n = int(input())
        for i in range(self.n):
            a = input()
            if "push" in a:
                self.push(a[-1])
            elif "pop" in a:
                self.pop()
            elif "size" in a:
                self.size()
            elif "top" in a:
                self.top()
            elif "empty" in a:
                self.empty()
    def push(self,a):
        self.stacklist.append(a)
    def pop(self):
        if self.empty():
            print(self.stacklist.pop())
        else:
            print(-1)
    def size(self):
        print(len(self.stacklist))
    def empty(self):
        if self.stacklist:
            print(0)
        else:
            print(1)
    def top(self):
        if self.empty():
            print(self.stacklist[-1])
        else:
            print(-1)
a = stack()
