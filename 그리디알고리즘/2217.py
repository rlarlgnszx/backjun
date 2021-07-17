class lope:
    lope_len =[]
    max = 0
    def __init__(self):
        self.n = int(input())
        self.lope_len = [int(input()) for i in range(self.n)]
        self.lope_len.sort()
        for i in range(len(self.lope_len)):
            if self.max < self.lope_len[i]*(len(self.lope_len)-i):
                self.max = self.lope_len[i]*(len(self.lope_len)-i)
        print(self.max)
a = lope()



