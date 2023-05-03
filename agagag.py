from itertools import product
a = [x for x in range(10)]
for i in a:
    print(i)
for i in range(len(a)):
    print(a[i])

for x in range(len(a)):
    for y in range(len(a)):
        print(a[x],a[y])


for x in range(len(a)):
    for y in range(x+1,len(a)):
        print(a[x],a[y])

b = list(product('012',repeat=2))
print(b)

for i in range(len(a)-1):
    if a[i]+a[i+1]>2:
        print(a[i]+a[i+1])

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
        print(a)


    
