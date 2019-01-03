# 1) program to count the number of vowels present in the string using set

str="HellO hI bYE Bye "
vowels=set("aeiouAEIOU")
count=0
for i in str:
    if i in vowels:
        count+=1
print("Vowels count :",count)
