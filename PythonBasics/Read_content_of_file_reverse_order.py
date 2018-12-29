#14) wap to read the content of a file in reverse order

from file_read_backwards import FileReadBackwards
with FileReadBackwards("E:/Python_Assignments/Demo.txt",encoding="utf-8") as f:

    for i in f:
        print(i)