# 4) wap to reverse the words of odd index value in a string

str1="hello hi how are you bye"
word=str1.split()
odd=[]
for i in range(len(word)):
    if i%2!=0:
        x=word[i]
        odd.append(x[::-1])
    else:
        odd.append(word[i])
print(odd)

