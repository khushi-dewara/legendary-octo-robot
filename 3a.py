#AIM:Remove all the lines that contain the character 'a' in a file and write  it to another file.
#to make sure the file is empty
open("test_res.txt", "w").close()
# make a file object in read mode
with open("test.txt" , "r") as test_file: 
data = test_file.readline()
    print(data)

    while(data):
        if(data.find("a") == -1):
          # make a file object in write mode  
          with open("test_res.txt" , "a")as test_file2: 
                test_file2.write(data+"\n")
            
        data = test_file.readline()
        print(data)
