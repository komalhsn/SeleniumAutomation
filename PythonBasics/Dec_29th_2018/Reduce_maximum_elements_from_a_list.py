#2) wap to find the maximum elements from a list using reduce
import functools

l = [10, 5, 40, 63]
p=functools.reduce(lambda a,b:a if a>b else b,l)
print(p)
