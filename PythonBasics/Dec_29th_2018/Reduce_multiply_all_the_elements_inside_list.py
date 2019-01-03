#1) wap to multiply all the elements inside a list using reduce
import functools

l = [10, 5, 42, 12]
p=functools.reduce(lambda a,b:a*b,l)
print(p)