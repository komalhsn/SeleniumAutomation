# 5 wap to mearg 2 list with sorted
# ex: l1=[1,2,5]
# l2=[1,3,2,4]
# o/p:
# [1,1,2,2,3,4,5]

import itertools
l1=[1,2,5]
l2=[1,3,2,4]
s=sorted([i for i in itertools.chain(l1,l2)])
print(s)