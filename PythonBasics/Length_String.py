# 4 wap to print a length of a string
# ex:
# ['hi','hello']
# o/p [(hi,2),(hello,5)]

s=['hi','hello','bye']
print([(i,len(i)) for i in s])
