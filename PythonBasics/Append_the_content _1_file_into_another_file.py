#16) wap to append the content of 1 file into another file

with open("E:/Python_Assignments/Demo.txt","r") as f:
    rd=f.read()
with open("E:/Python_Assignments/Demo1.txt","a") as f1:
    wr=f1.write(rd)
    print(wr)



