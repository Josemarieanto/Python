##l = [2,4,6,8]
##x = 0
##def sum():
##    global x
##for i in range(len(l)):
##    x += l[i]
##print(x)
##sum()
##l = [2,4,6,8]
##x = 0
##def subtract():
##    global x
##for i in range(len(l)):
##    x -= l[i]
##print(x)
##subtract()
##l = [2,4,6,8]
##x = 1
##def multiplication():
##    global x
##for i in range(len(l)):
##    x *= l[i]
##print(x)
##multiplication()
##l = [2,4,6,8]
##x = 1
##def division():
##    global x
##for i in range(len(l)):
##    x /= l[i]
##division()
##print(x)
##n = [1,2,3,3,4,5]

##def value_equal_to_index(n):
##    position = 1 
##    for i in n:
##        position += 1
##index = 3
##value = n[index - 1]
##if value == index:
##    print(index , ":"  , value)
##else:
##    print("no match found")
##value_equal_to_index(n)
##l = [1,2,3,4,5]
##def valueEqualToIndex(list):
##    newList = []
##    l = len(l)
##    for i in range(l):
##        index1Based = i + 1
##        element = list[i]
##        if element == index1Based:
##            newList.append(list[i])
##    return newList
# ##valueEqualToIndex(list)
# l = 1234568
# print(l % 10)
# x = 
# print(l / 10)


#def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x - 1))
# num = 5
# print(factorial(num))



#def countdown(value):
#   if value <= 0:   #base case  
#     print("done")
#   else:
#     print(value)
#     countdown(value-1)


# def printNumber(n):
#   if n > 0:
#     printNumber(n - 1)
#     print(n, end = ' ')
# n = 10  
# printNumber(n - 1)

# def countdown(n):
#     print(n)
#     if n == 0:
#         return 0
#     return countdown(n - 1)
# countdown(5)


# def series(N, n=0):
#     print(n)
#     if n < N:
#         series(N, n + 1)
# series(5)


# list comprehension:

# squares = [x**2 for x in range(10)]
# print(squares)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# s = {v for v in 'ABCDABCD' if v not in 'AD'}
# print(s)

# n = [1,2,3,4,5]
# squared_numbers = [i * i  for i in n]
# print(squared_numbers)
# n = [1,2,3,4,5,6,7,8,9,10]
# even_num = [i for i in n if i % 2 == 0]
# odd_num = [i for i in n if i % 2 != 0]
# print(even_num)
# print(odd_num)

# word = "josemarie"
# vowels = "aeiou"
# output = [i for i in word if i in vowels]
# print(output)

## map,filter and reduce:

# strings = ["1", "2", "3", "4", "5"]
# numbers = list(map(int, strings))
# print(numbers)


# from functools import reduce
# numbers = [1, 7, 3, 9, 5]
# max_number = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_number)

# numbers = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x % 2 == 0:
#     return False
#   else:
#     return True

# odd = filter(myFunc, numbers)

# for x in odd:
#   print(x)

# def myfunc(a,b):
#     return a + b
# sum = map(myfunc, (1,2,3,4,5),(6,7,8,9,10))
# print(list(sum))

#x = ["ab","cd","ef"]
# uppered_x= []
# for i in x:
#     y = i.upper()
#     uppered_x.append(y)
# print(uppered_x)
#uppered_x = map(str.upper,x)     
#print(list(uppered_x))
# l = [1,2,3,4,5]
# def doubled_num(num):
#     return num*2
# def tripled_num(numbers):
#     return numbers * 3 


# def hof(l,func):
#     output = []
#     for i in l:
#         output.append(func(i))
#     return output

    

# print(hof(l,doubled_num))
# print(hof(l,tripled_num))
# print(list(map(doubled_num,l)))
# print(list(map(tripled_num,l)))

# x = [1,21,22,13,24,15]
# def myfunc(x):
#         if x < 20:
#             return True
#         return False
    
# output = filter(myfunc, x)
# print(list(output))
# l = [1,2,3,4,5]
# def myfunc(l):
#     if l < 4:
#         return True
#     return False
    
        
# def hof(l,func):
#     output = []
#     for i in l:
#         if(func(i)):
#             output.append(i)
#     return output

    

# print(list(filter(myfunc,l)))

# def kLargest(arr, k):
# 	arr.sort(reverse=True)
# 	for i in range(k):
# 		print(arr[i], end=" ")


# arr = [1, 23, 12, 9, 30, 2, 50]
# k = 3
# kLargest(arr, k)



        


    

   
        














