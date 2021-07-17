#백트래킹 알고리즘입니다.
#백트래킹이란 조합중에 모든조합이아닌 조건을 정해서
#조합을 설정하는 경욷의수
#하지만 실패!
class big:
    def __init__(self,start,end) :
        self.start=start
        self.end = end
        self.bigger=False


class comute:
    promise =[]
    def __init__(self):
        self.n = int(input())
        for i in range(self.n):
            start,end = map(int,input().split())
            self.promise.append(big(start,end))
        self.sort()
        self.start()
    def sort(self):
        for i in range(len(self.promise)-1):
            for j in range(i+1,len(self.promise)):
                if self.promise[i].start > self.promise[j].start:
                    if self.promise[i].end < self.promise[j].end :
                        self.promise[j].bigger = True
                    self.promise[i],self.promise[j]=self.promise[j],self.promise[i]

                elif self.promise[i].start == self.promise[j].start:
                    if self.promise[i].end >self.promise[j].end:
                        self.promise[i],self.promise[j]=self.promise[j],self.promise[i]
                        self.promise[j].bigger = True
    def print(self):
        for oi in self.promise:
            print(oi.start,oi.end , oi.bigger)
    def checking(self,a):
        classlist=[a]
        for i in self.promise:
            if i.bigger ==False and classlist[-1].end <=i.start:
                classlist.append(i)
        return classlist
    def start(self):
        max = 0
        for i in self.promise:
            if i.bigger ==False:
                if len(self.checking(i)) >max:
                    max = len(self.checking(i))
        print(max)
############다시 생각 시간초과 나옴"
n = int(input())
time = [list(map(int,input().split())) for x in range(n)]
time = sorted(time,key=lambda time:time[0])
time = sorted(time,key=lambda time:time[1])
real = 0
last =0
for i in time:
    if i[0]>=last:
        last = i[1]
        real +=1
print(real)


        
        