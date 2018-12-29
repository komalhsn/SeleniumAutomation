for i in range(1,1000):
    if i>2:
       for j in (2,i+1):
         if i%2==0:
            break
       else:
          print(i)