# 2) wap to count the number of lowercase character in the string

str="WeaTheR Is NOT good ToDaY"
count=0

for i in str:
    if (i.islower()):
        count=count+1
print(count)