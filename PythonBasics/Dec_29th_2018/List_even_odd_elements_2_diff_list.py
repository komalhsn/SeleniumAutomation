#3) wap to even and odd elements in a list in to 2 different list

lst=[2,5,6,4,9,6,25,47]
even=[]
odd=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print (even)
print (odd)