#별찍기
def star(n):
    mid = int(n/3)
    if n==3:
        for i in range(n):
            for j in range(n):
                if i==n/3 and j==n/3:
                    print(" ",end="")
                else:
                    if j==n-1:
                        print("*")
                    else:
                        print("*",end="")
                    
    elif n>3:
        new = int(n/3)
        for i in range(n):
            for j in range(n):
                if int(i/3)==new:
        
star(3)
