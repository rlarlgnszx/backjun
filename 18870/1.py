"""
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다.
 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는
 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과
 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이
 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 
구분해서 출력한다.
"""
#from dataclasses import datacases
class id:
    value=[]
    count =0
    def __init__(self,val):
        self.val =val
        self.zip=0
        if len(self.value)>0:
            for i in range(len(self.value)):
                if self.value[i].val> self.val:
                    self.value[i].zip +=1
                elif self.value[i].val<self.val:
                    self.zip +=1
            self.value.append(self)
        else:
            self.value.append(self)
    def print(self):
        print("배열값 :",end="")
        for i in range(len(self.value)):
            print(self.value[i].val, end= " ")
        print()
        print("압축값 :",end="")
        for i in range(len(self.value)):
            print(self.value[i].zip, end= " ")
#실패!
    
    
n = int(input())
xlist = list(map(id,input().split()))
xlist[0].print()




        
    