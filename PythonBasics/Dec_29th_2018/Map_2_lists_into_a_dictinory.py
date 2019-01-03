# 2) wap to map 2 lists into a dictinory

l=[1,2,3,4]
l1=['a','b','c','d']

d={x:y for x,y in zip(map(int,l),map(str,l1))}
print(d)