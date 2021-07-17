#hanoi
class hanoi:
    count =0
    def __init__(self):
        pass
    def start(self,n,now,to,move):
        self.count+=1
        if n==1:
            print(now,move)
        else:
            self.start(n-1,now,move,to);
            print(now,move)
            self.start(n-1,to,now,move);
    def start2(self,n,now,to,move):
        self.count+=1
        if n==1:
            #print(now,move)
            pass
        else:
            self.start2(n-1,now,move,to);
            #print(now,move)
            self.start2(n-1,to,now,move);
a = hanoi()
n = int(input())
a.start2(n,1,2,3)
print(a.count)
a.start(n,1,2,3)



