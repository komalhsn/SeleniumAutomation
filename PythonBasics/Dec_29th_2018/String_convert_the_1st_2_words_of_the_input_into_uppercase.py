# 1) wap  to convert the 1st 2 words of the input into uppercase

str="weather is good today"
wrd=str.split()
count=0
for i in wrd:
    print(i.upper())
    count+=1
    if count>1:
        break

