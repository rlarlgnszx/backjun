
class move:
    movelist=[]
    count =0
    def __init__(self):
        self.n =int(input())
        for i in range(self.n):
            self.movelist.append(list(map(int,input().split())))
        for j in self.movelist:
            print(self.result(j[0],j[1]))

    def result(self,start,end):
        count =0
        speed =1
        mid = (start+end)/2
        while start<=end:
            start +=speed*2
            count *=2
            if start==mid:
                count *
        #3일경우 1,1,1
        #4일경우 1,2,1
        #5일경우 1,2,1,1
        #6일경우 1,2,2,1
        #7일경우 1,2,2,1,1
        #8일경우 1,2,2,2,1
        #9일경우 1,2,3,2,1
        #10일경우 1,2,3,2,1,1
        #11일경우 1,2,3,2,2,1
        #12일 경우 1,2,3,3,2,1
        #13일경우 1,2,3,3,2,1,1
        #14일경우 1,2,3,3,2,2,1

a = move()



        
