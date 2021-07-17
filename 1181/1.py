"""알파벳 소문자로 이루어진 N개의 단어가 들어오면
 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로"""

n = int(input())
class sub:
    word=""
    len2=0
    def __init__(self,a):
        self.word=a
        self.len2 = len(a)

class word(sub):
    xlist =[]
    def __init__(self,a):
        self.xlist.append(sub(a))

    def print2(self):
        for x in range(len(self.xlist)):
            print(self.xlist[x].word)
    def sort2(self):
        for i in range(len(self.xlist)):
            #key = self.xlist[i]
            for j in range(i):
                if self.xlist[j].len2==self.xlist[i].len2:
                    if self.xlist[j].word > self.xlist[i].word:
                        self.xlist[j],self.xlist[i]=self.xlist[i],self.xlist[j]
                        #self.print2()
                        #print("\n")
                elif self.xlist[j].len2 > self.xlist[i].len2 :
                        self.xlist[j],self.xlist[i]=self.xlist[i],self.xlist[j]
                        #self.print2()
                        #print("\n")
                    
"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""
            

for i in range(n):
    a = word(input())
print("출력값 :")
a.sort2()
a.print2()


