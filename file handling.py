# f = open("test.txt","x")
# 1

# f = open("test.txt","w")
# f.write("the file test.txt created successfully")
# f.close()
# f = open("test.txt","r")
# print(f.read())

# 2

# f = open("test.txt","r")
# print("this is the content of the file test.txt")
# f.close()

# 3

# f = open("test.txt","w")
# f.write("test line 1 \n test line 2 \n test line 3 \n test line 4 \n")
# f.close()
# f = open("test.txt","r")
# print(f.read())

# 4


# f = open("test.txt","w")
# f.write("test line 1 \n test line 2 \n test line 3 \n test line 4 \n")
# f.close()
# f = open("test.txt","r")
# array = []
# for i in f :
#     array.append(i)
# print(array)

#  5

# f = open("test.txt","w")
# f.write("test line 1 \n test line 2 \n test line 3 \n test line 4 \n")
# f.close()
# f = open("test.txt","r")
# lines = len(f.readlines())
# print("the number of lines in this file: ",lines)
# f.close()

#  6

# f = open("test.txt","w")
# f.write("test line 1 \n test line 2 \n test line 3 \n test line 4 \n")
# f.close()
# f = open("test.txt","r")
# content = f.read()
# f = open("test.txt","r")
# lines = len(f.readlines())
# print(content)
# print("the number of lines in this file: ",lines)
# f.close()

#  7

# f = open("test.txt","w")
# f.write("test line 1\ntest line 2\ntest line 3\ntest line 4")
# f.close()
# f = open("test.txt","r")
# content = f.read()
# word_count = len(content.split())
# char_count = len(content)

# print(content)
# print("the number of words",word_count )
# print("the number of characters",char_count)
# f.close()

#  8 
	
# f = open("test.txt","r")
# content = f.readlines()
# print(content)
# content[1] = "test line 2\n"
# f = open("test.txt","w")
# f.writelines(content)

#  9

# f = open("test.txt","a")
# f.write("test line 2")
# f.close()
# f = open("test.txt","r")
# print(f.read())

#  10

# f = open("test.txt","w")
# f.write("test line 1\ntest line 2\ntest line 3\ntest line 4\n")
# f.close()
# f = open("test.txt","a")
# f.write("\ntest line 5\ntest line 6\ntest line 7")
# f.close()
# f = open("test.txt","r")
# print(f.read())

#  11

# import os

# source = "test.txt"
# dest = "test1.txt"
# os.rename(source,dest)
##f = open("test1.txt","r")
##print(f.read())
