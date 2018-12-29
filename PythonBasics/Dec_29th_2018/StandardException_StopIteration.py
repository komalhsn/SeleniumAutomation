# z = [5, 9, 7]
# i = iter(z)
# print (i)
# print (next(i))
# print (next(i))
# print (next(i))
# print (next(i))


#above code gives stopiteration to avoid it

try:
    l = [15, 25, 35]
    i = iter(l)
    print (next(i))
    print (next(i))
    print (next(i))
    print (next(i))
except Exception as e:
    print (type(e))