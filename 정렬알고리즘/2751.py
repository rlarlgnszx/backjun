#병합정렬을 사용? 어떤건지 ㅗㅁ르겟구나
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