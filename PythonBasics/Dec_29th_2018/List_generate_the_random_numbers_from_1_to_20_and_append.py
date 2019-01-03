#5) wap to generate the random numbers from 1 to 20 and append them to list


import random as r
lst=[]
for i in range(5):
    a=r.randint(1,20)
    lst.append(a)
print(lst)