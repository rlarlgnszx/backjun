x = int(input())
listx = [int(input()) for t in range(x)]
print()
print("산술평균 :",round(sum(listx)/x))
listx.sort()
print("중앙값 ",listx[int(len(listx)/2)],"   리스트는 :",listx)
countlist=[listx.count(listx[t]) for t in range(x)]
listx2=listx[:]
if countlist.count(max(countlist))>=2:
    listx2.pop()
countlist=[listx2.count(listx2[t]) for t in range(len(listx2))]
print("최빈값 :",listx2[countlist.index(max(countlist))])

print("범위 :",max(listx)-min(listx))