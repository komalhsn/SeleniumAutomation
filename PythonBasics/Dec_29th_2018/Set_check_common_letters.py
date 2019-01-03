#2) WAP to check common letters in two input strings

s1=input("Enter the 1st string:")
s2=input("Enter the 2nd string:")
commonset=set(set(s1)&set(s2))
if len(commonset)>0:
    print("Common letters present in two input strings")
print(commonset)