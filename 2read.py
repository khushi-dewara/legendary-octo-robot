#AIM: read a file line by line and print it.

myfile=open(r'E:\poem.txt',"r")
str=" " #initially storing a space (any non-None value)
while str:
    str=myfile.readline()
    print(str,end='')
    
myfile.close()
