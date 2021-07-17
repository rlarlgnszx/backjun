"""온라인 저지에 가입한 사람들의 
나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다.
 (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 
공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며,
 200보다 작거나 같은 정수이고, 이름은
  알파벳 대소문자로 이루어져 있고, 
  길이가 100보다 작거나 같은 문자열이다. 
  입력은 가입한 순서로 주어진다.
"""
#from dataclasses import dataclass
class name_old:
    name=""
    old=0
    def __init__(self,old,name):
        self.name =name
        self.old = old
class person:
    personlist=[]
    def __init__(self):
        pass
    def add(self,nameold):
        self.personlist.append(nameold)
    
    def print(self):
        for i in self.personlist:
            print(i.old, " ", i.name)
    def sort2(self):
        for i in range(len(self.personlist)-1,1,-1):
            for j in range(i):
                if self.personlist[j].old >= self.personlist[i].old:
                    self.personlist[i],self.personlist[j]=self.personlist[j],self.personlist[i]
                    
    #주의점 그냥 정렬할경우 가입순으로 정렬이 안된다
    #그럴 경우 한꺼번에 옮기는 경우가 필요
    #헷갈림주의 stable sort

n = int(input())
for i in range(n):
    old,name = input().split()
    a = name_old(old,name)
    b = person()
    b.add(a)
b.sort2()
b.print()
