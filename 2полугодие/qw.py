import sys
sys.setrecursionlimit(3000)

def f(n):
    if n == 1:
        return 1
    elif n >1 :
        return n*f(n-1)
    



a=f(2023)
b=f(2020)
print(a/b)
