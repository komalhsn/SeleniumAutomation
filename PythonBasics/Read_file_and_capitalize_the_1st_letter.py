#15) wap to read file and capitalize the 1st letter of every word in the file

with open("E:/Python_Assignments/Demo.txt","r") as f:
    for i in f:
        l=i.title()
        print(l)