"""
문제
N개의 수가 주어졌을 때,
 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
  수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 
한 줄에 하나씩 출력한다.
"""
class sort:
    list =[]
    def __init__(self):
        n = int(input())
        for i in range(n):
            a = int(input())
            if i==0:
                self.list.append(a)
            else:
                self.mysort(self.list,a)
        print(self.list)
    def mysort(self,list2,a):
        for i in range(len(self.list)):
            if self.list[i]>a:
                self.list.insert(i,a)
                break
            elif i==len(self.list) and self.list[i]<a:
                self.list.append(a)
                break

a =sort()


        

        
