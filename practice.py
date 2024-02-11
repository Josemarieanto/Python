##n  = 5
##def seriessum(n):
##    seriessum = 0
##    for i in range(1,n+1):
##        seriessum += i
##    return seriessum
##result = seriessum(n)
##print(result) """
##""" l = [2,4,6,8,10]
##def print_alternate_elements(arr):
##    for i in range(0, len(arr), 2):
##        print(arr[i],end = "  ")
##print_alternate_elements(l)
##l = [1, 2, 3, 4, 5] 
##def print_left_element(arr):
##    if arr:
##        print("Left element:", arr[0])
##    else:
##        print(" ")
##print_left_element(l)
##
##l = [10,20,30,40,50,60]
##def find_element_at_index(arr):
##        print(arr[2])
##find_element_at_index(l)        
##l = [
##    [1,2,3,2,1],
##    [1,2,3,4,5]
##]
##def isperfect(arr):
##    return (arr[0]) == (arr[-1])
##for arr in l:
##    if isperfect(arr):
##        print("Perfect Array:", arr)
##    else:
##        print("Not a Perfect Array:", arr)
##isperfect(l)
##l = [12,2]
##def stream_average(arr):
##    total_sum = 0
##    count = 0
##    for i in arr:
##        total_sum += i
##        count += 1
##        average = total_sum / count
##        print(average,end = " ")
##stream_average(l)
##n = [1,2,3,4,5]
##def average(n):
##    total = 0
##    for i in n:
##        total += i
##        avr = total/len(n)
##    print("Total: ",total, "Average: " , avr)
##average(n)
##n = [1,2,3,4,5]
##def value_equal_to_index(n):
##    position = 1
##    for i in n:
##        position += 1
##index = 2
##value = n[index - 1]
##if value == index:
##    print(index , " : " , value)
##value_equal_to_index(n)
##a = 10

#def countdown(n):
     ##print(n)
    ## if n == 0:
 ##         return             # Terminate recursion
 ####    else:
 ##      countdown(n - 1)   # Recursive call


##countdown(5)


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return(x * factorial(x - 1))
    
# num = 4
# print("the factorial of",num,"is",factorial(num))

##HOF:
# Python program to illustrate functions 
# can be treated as objects 
# def shout(text): 
# 	return text.upper() 
	
# print(shout('Hello')) 
	
# # Assigning function to a variable 
# yell = shout 
	
# print(yell('world')) 

# Python program to illustrate functions 
# can be passed as arguments to other functions 
# def shout(text): 
# 	return text.upper() 
	
# def whisper(text): 
# 	return text.lower() 
	
# def greet(func): 
# 	# storing the function in a variable 
# 	greeting = func("Hi, I am created by a function passed as an argument.") 
# 	print(greeting) 
	
# greet(shout) 
# greet(whisper) 

# a = [134, 43, 56, 2, 3, 5, 6, 32, 65, 123]


# def func(i):
#     if i > 20:
#         return False
#     return True


# f = filter(func, a)

# print(list(f))
#l1 = [4, 3, 2, 6, 7, 20, 5, 36, 24, 92]


# def filterList(n):
#     l = []
#     for i in n:
#         if (i <= 20):
#             l.append(i)
#     return l


# print(filterList(l1))


# def myFunc(i):
#     if (i <= 20):
#         return True
#     return False


# fltr = filter(myFunc, l1)
# print(list(fltr))

# l1 = [4, 3, 2, 6, 7, 5]
# l2 = [23, 10, 4, 11, 8, 3]


# def double(l):
#     a = []
#     for i in l:
#         a.append(i ** 2)
#     return a


# def triple(l):
#     a = []
#     for i in l:
#         a.append(i ** 3)
#     return a
# print("double")
# print(double(l1))
# print(double(l2))
# print("triple")
# print(triple(l1))
# print(triple(l2))

# from functools import reduce
# l = [1, 2, 3, 4, 5]


# def sum(l):
#     a = 0
#     for i in l:
#             a += i
#     return a

# print(sum(l))
# from functools import reduce 

# l = [1,2,3,4,5]
# def sum(x,y):
#     for i in l:
#         return x + y
    
# output = reduce(sum,l)
# print(output) 

# l = [1,2,3,4,5]
# def nums(x):
#     for i in l:
#         if i % 2 == 0:
#             return True
#         return False 
    
# output =filter(nums,l)
# print(list(output))
# l =[2,3,4,5,6]
# def higher(nums):
#     if  nums > 5:
#           return True
#     return False

# def hof(l,func):
#     output = []
#     for i in l:
#         output.append(func(i))
#     return output

# print(list(filter(higher,l)))
# l =[2,3,4,5,6]
# def higher(nums):
#     if  nums > 5:
#           return True
#     return False

# def hof(l,func):
#     output = []
#     for i in l:
#         output.append(func(i))
#     return output

# print(list(map(higher,l)))
# x = 5
# sum = lambda a : a + x
# print((sum(3)))


# double = lambda a,b:a + b 
# print(double(2,3))

# def add(a):
#     return lambda b : a * b

# double= add(2)
# triple = add(3)

# print(double(5))
# print(triple(5))

# def num(a , b):
#     return  a + b

# sum = lambda a , b : a + b
# print(sum(3,7))
























































    



