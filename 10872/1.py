#팩토리얼
def fac(n):
    if n==0:
        return 1
    elif n<=2:
        return n
    return fac(n-1)*n
n = int(input())
print(fac(n))
