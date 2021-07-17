"""2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음
 출력하는 프로그램을 작성하시오."""

n = int(input())
class point():
    pointlist=[]

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print(self):
        for i in self.pointlist:
            print(i.x," ",i.y)

    def sortpoint(self):
        for i in range(len(self.pointlist)-1):
            for j in range(i+1,len(self.pointlist)):
                if self.pointlist[i].x==self.pointlist[j].x :
                    if self.pointlist[i].y > self.pointlist[j].y :
                        self.pointlist[i], self.pointlist[j] = self.pointlist[j], self.pointlist[i]
                elif self.pointlist[i].x > self.pointlist[j].x :
                    self.pointlist[i], self.pointlist[j] = self.pointlist[j], self.pointlist[i]

for i in range(n):
    x,y =map(int,input().split())
    pointl = point(x,y)
    pointl.pointlist.append(pointl)
#입력값
"""5 
3 4
1 1
1 -1
2 2
3 3
"""
pointl.print()# 원래 포인트객체리스트값
pointl.sortpoint()# 포인트 리스트 정렬
pointl.print() # 포인트 리스트 출력
