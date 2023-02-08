from itertools import product
def f(x,y,z):
    count = 0
    for i in range(2,z):
        b = product('12', repeat = i)
        print(i)
        input()
        for n in b:
            if x == 10 and n.count('2'):
                continue
            a= int(x)
            for v in n:
                if v == '1': a+=1
                else: a*=2
            if a == 17:
                break
            if a == y:
                count+=1
    return count

print (f(10,35,25))
