#1) wap to read a list of word and return the length of the longest one

n=int(input("Enter the number of words "))
wrd=[]
Length=[]
for i in range(n):
    x=input("Enter the words")
    wrd.append(x)
    Length.append(len(x))
print("words are",wrd)
print("Length of each words are",Length)
print("Longest word is",max(Length))