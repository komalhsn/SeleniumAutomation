# f=open("ntihi.txt",'r')
#
# f.write("Hi")

#Above code produces IO.Unsupported Error file is opened for reading and write operation not permitted

try:
    f=open("ntihi.txt",'r')
    f.write("Hi")
except Exception as e:
    print(type(e))