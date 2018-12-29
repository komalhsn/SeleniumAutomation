#7 wap to remove the duplicate value from the list

s=[2,5,6,8,5,2,6,4,9]
s1=[]
[s1.append(i) for i in s if i not in s1 ]
print(s1)