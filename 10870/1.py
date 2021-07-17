#피보나치
def fib(n):
    if n==0:
        return 0
    elif n<=2:
        return 1
    else:
        return fib(n-2) + fib(n-1)
n = int(input())
print(fib(n))

#성공