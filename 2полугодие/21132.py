with open('17.txt') as f:
    nums = [int(x) for x in f]
    nums = list(map(abs,nums))
    count = 0
    sp = []
    sp2=[]
    for x in nums:
        if x%10==3:
            sp.append(x)

maxi = max(sp)
        
for i in range(len(nums)-1):
    if ((nums[i]%10==3 and nums[i+1]%10!=3) or (nums[i]%10!=3 and nums[i+1]%10==3)) and (nums[i]**2+nums[i+1]**2>=maxi**2):
        count+=1
        sp2.append(nums[i]**2+nums[i+1]**2)

print(count,max(sp2))




        




    
        
