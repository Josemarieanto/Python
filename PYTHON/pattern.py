####rows = 5
####for i in range(rows):
####    for j in range()
# for i in range(1, 6):
#    for j in range(i + 5):
#        print(i, end=' ')
#    print()
# rows = 5
# for i in range(1, rows + 1):
#    for j in range(i + 1):
#        print(i,j, end='  ')
#    print()
# for i in range(1, 6):
#    # nested loop
#    # to iterate from 1 to 10
#    for j in range(i ++ 5):
#        # print multiplication
#        print(i+  j)
#    print()
# rows = 5
# for i in range(1, rows + 1):
#    for j in range(1, rows + 5):
#        if j <= i:
#            print(i, end=' ')
#        else:
#            print(j, end=' ')
#    print()
##
# s = int(input("Please enter the number of rows :  "))  
# for i in range(1,6):  
#    for j in range(1,s +5):  
#        print(j, end=' ')  
#    print()   
# for i in range(1, 26):
#    for j in range(i + 5):
#        print("{:2d}". format(j), end = " ")
# print()        
####num = int(input("Enter the Number: "))
####
####for i in range(num):
####    for j in range(i):
####        print(j +5, end="")
####    print()
##
####for i in range(1,26):
####    for j in range(i+5):
####        print(j, end=' ')
####    print() 
####for i in range(1,26):
####    for j in range(i):
####        print(j+1, end=" ")
####    print()
####k = 1
####for i in range(0, 5):
####    for j in range(0, i+1):
####        print(k, end=" ")
####        k = k + 1
####    print()
####for i in range(0, 5):
####    num = 1
####    for j in range(0, i+1):
####        print(num, end=" ")
####        num = num + 1
####    print()
# numb = 1
# inc = 1
# for i in range(0, 5):
#    for j in range(0, inc):
#        print(numb, end=" ")
#    numb = numb + 1
#    print()
#    inc = inc + 2
####
##
# numb = 1
# inc = 1
# for i in range(0, 5):
#    for j in range(0, inc):
#        print(numb, end=" ")
#        numb = numb + 1
#    print()
#    inc = inc + 2
######--------------------------------------------------------
# last_num = 9
# for i in range(1, last_num):
#    for j in range(-1+i, -1, -1):
#        print(format(2**j, "4d"), end=' ')
#    print("")
# n = 5
# for i in range(1, 26,5):
#    for j in range(i+5):
#        print(i * j, end="\t")
#    print()
# def print_custom_square_pattern(rows, columns, start, step):
#    for i in range(1, rows + 1):
#        for j in range(1, columns + 1):
#            print(start + (i - 1) * columns * step + (j - 1) * step, end="\t")
#        print()

# # Example: Printing the sequence 2, 7, 12, 17, and 22 in a square pattern
# print_custom_square_pattern(1, 5, 1, 5)
####def print_custom_square_pattern(rows, columns, start, step):
####    for i in range(1, rows + 1):
####        for j in range(1, columns + 1):
####            print(j, end = " ")
####        print()
####
##### Example: Printing the specified pattern
####rows = 5
####columns = 5
####start = 1
####step = 5
####print_custom_square_pattern(rows, columns, start, step)
####
# rows = 5
# columns = 5

# for i in range(1, rows + 1):
#    for j in range(1, columns + 1):
#        print(i + (j - 1) * rows, end="\t")
#    print()
# for i in range(1,6):
#    for j in range(0,5):
#        print(i + j * 5, end = " ")
#    print()    
# for i in range(5,0,-1):
#    for j in range(0,5):
#        print("{:2d}". format(i + j * 5), end = " ")
#    print()    
# for i in range(1,6):
#    for j in range(0,5):
#        print(i + j, end = " ")
#    print()
# for i in range(1,10,2):
#    for j in range(0,10,2):
#        print("{:2d}". format(i + j) , end = " ")
#    print()    
# for i in range(0,2):
#    for j in range(1,0):
#        print(i,j,end = " ")
#    print()
####for i in range(5):
####    for j in range(5):
####        if (i + j) % 2 == 0:
####            print("0", end=' ')
####        else:
####            print("1", end=' ')
####    print()
####for i in range(1,6):
####    for j in range(0,1):
####        if(i + j == 0):
####            print("1", end = " ")
####        else:
####            print("0",end = " ")
####    print()
# for i in range(1,0):
#    for j in range(0):
#        print(i,j)
#    print()
# for i in range(1,6):
#    for j in range(1,6):
#        if(i % 2 == 0):
#            print("1", end = " ")
#        else:
#            print("0",end = " ")
#    print()
####x = 0
####y = x + 1
####for i in range(1,6):
####    for j in range(1,6):
####        if((i + j) % 2 == 0):
####            print(x, end = " ")
####        else:
####            print(y,end = " ")
####    print()
####for i in range(5):
####    for j in range(5):
####        print(chr(69 - i), end = " ")
####    print()
# x = 0
# for i in range(5):
#    for j in range(5):
#        print((chr(65 + x)),end = ' ')
#        x += 1
#    print()
####print(" pattern : 32")
####for i in range(5):
####    for j in range(5):
####        print(chr(65 + i + j * 5),end = " ")
####    print()    
####print(" pattern : 33")
####for i in range(5):
####    for j in range(5):
####        print(chr(69 - i + j * 5),end = " ")
####    print()
####print(" pattern : 41")
# x = 1
# for i in range(1,5):
#    for j in range(1,x + 1):
#        print(j, end = " ")
#        x += 1
#    print()
####print("pattern 43")
# x = 1
# for i in range(1,6):
#    for j in range(i):
#       print(x+1,end = " ")
#       x += 2
#    print()
####print("pattern :48")
# for i in range(1,16,5):
#    x = i
#    for j in range(i):
#        print(x ,end = " ")
#        x -=i
#    print()    
####for i in range(5):
####    for j in range(9):
####        if(i in{0})and(j in {4}):
####            print("* ", end = " ")
####        elif(i in {1})and(j in{3,5}):
####            print("* ", end = " ")
####        elif(i in {2})and(j in{2,3,4,5,6}):
####            print("* ", end = " ")
####        elif(i in {3})and(j in{1,7}):
####            print("* ", end = " ")
####        elif(i in {4})and(j in{0,8}):
####            print("* ", end = " ")    
####        else:
####            print("  ", end = " ")   
####    print()        
##print(" pattern : 50")
##for i in range(1,6):
##    for j in range(1,6):
##        if(i in {1} and j in {1}):
##            print(" 5 ",end = " ")
##        elif(i in {2})and(j in{1}):
##            print(" 6 ", end = " ")
##        elif(i in {2})and(j in{2}):
##            print("  4 ", end = " ")
##        elif(i in {3})and(j in{1}):
##            print(" 12 ", end = " ")
##        elif(i in {3})and(j in{2}):
##            print(" 7 ", end = " ")
##        elif(i in {3})and(j in{3}):
##            print("  3 ", end = " ")
##        elif(i in {4})and(j in{1}):
##            print(" 13 ", end = " ")
##        elif(i in {4})and(j in{2}):
##            print(" 11 ", end = " ")
##        elif(i in {4})and(j in{3}):
##            print(" 8 ", end = " ")
##        elif(i in {4})and(j in{4}):
##            print("  2 ", end = " ")
##        elif(i in {5})and(j in{1}):
##            print(" 15 ", end = " ")
##        elif(i in {5})and(j in{2}):
##            print(" 14 ", end = " ")
##        elif(i in {5})and(j in{3}):
##            print(" 10 ", end = " ")
##        elif(i in {5})and(j in{4}):
##            print(" 9 ", end = " ")
##        elif(i in {5})and(j in{5}):
##            print(" 1 ", end = " ")
##        else:
##            print("  ", end = " ")
##    print()
# rows = 5
# num = 1
# ####
# for i in range(1, rows + 1):
#    for j in range(1, i + 1):
#        print(num, end=" ")
#        num += 1
#    print()

for i in range(0,7):
    for j in range(0,7):
        if(i in {0} and j in {3}):
           print(" 1 ",end = " ")
        elif(i in {1})and(j in{2}):
           print(" 2 ", end = " ")
        elif(i in {1})and(j in{4}):
           print(" 3 ", end = " ")
        elif(i in {2})and(j in{1}):
           print(" 4 ", end = " ")
        elif(i in {2})and(j in{3}):
           print(" 5 ", end = " ")
        elif(i in {2})and(j in{5}):
           print(" 6 ", end = " ")
        elif(i in {3})and(j in{0}):
           print(" 7 ", end = " ")
        elif(i in {3})and(j in{2}):
           print(" 8 ", end = " ")
        elif(i in {3})and(j in{4}):
           print(" 9 ", end = " ")
        elif(i in {3})and(j in{6}):
           print(" 10 ", end = " ")
        else:
           print("  ", end = " ")
    print()


