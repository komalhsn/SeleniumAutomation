# 2) wap to find all numbers in a range which are perfect squares and sum of all digits in the number are less than 100

import math

for i in range(5):
    sq=int(math.sqrt(i))
    if i==sq*sq:
        print(i, " is perfect square")
    else:
        print(i,"not a perfectsquare")