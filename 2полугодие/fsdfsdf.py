spisok=[]
for i in range(2,1000):
  n=0
  for x in range (2,100):
    if i%x==0:
        n+=1
    
  
  if n==0:spisok.append(i)
        
flag=False
for i in spisok:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y)
            flag=True
