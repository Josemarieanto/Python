# # fizzbuzz program:

# # n = int(input())

# # for i in range(1,n+1):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print("fizzbuzz")
# #     elif i % 3 == 0:
# #         print("fizz")
# #     elif i % 5 == 0:
# #         print("buzz")
# #     else:
# #         print(i)

# #  palindrome program:

# # s = input("")

# # if s == s[::-1]:
# #     print("yes")
# # else:
# #     print("no")

# # factorial:

# # def factorial(x):
# #     if x == 1:
# #         return 1
# #     else:
# #         return x * factorial((x - 1))
# # num = int(input())
# # print(factorial(num))

# # rev string:

# # def revstring(str):
# #     return str[::-1]

# # rev = input()
# # print(revstring(rev))

# #  anagram program:

# # def anagram(s1, s2):
# #     if sorted(s1) == sorted(s2):
# #         return "yes"
# #     else:
# #         return "no" 
# # str1 = input()
# # str2 = input()

# # print(anagram(str1, str2))


# # removing duplicate:

# # n = list(map(int, input("Enter space-separated integers: ").split()))
# # l = list(dict.fromkeys(n))
# # print(l)

# # two sums:
# # def two_sums(n,t):
# #     for i in range(len(n)):
# #         for j in range(i+1,len(n)):
# #             if n[i]+n[j] == t:
# #                 return i, j

# # l = [5,4,1,2,6]
# # print(two_sums(l,3))

# # reverse integer:
# n = 12345332
# rev = 0

# lastNum = n % 10
# rev = rev * 10 + lastNum
# n = n // 10

# lastNum = n % 10
# rev = rev * 10 + lastNum
# n = n // 10

# lastNum = n % 10
# rev = rev * 10 + lastNum
# n = n // 10

# # lastNum = n % 10
# # rev = rev * 10 + lastNum
# # n = n // 10


# # while n != 0:
# #     lastNum = n % 10
# #     rev = rev * 10 + lastNum
# #     n = n // 10


# print(n, "n")
# print(rev, "rev")

# checking vowels:

# vowel = ["a","e","i","o","u"]
# word = "josemarie"
# count = 0
# for i in word:
#     if i in vowel:
#         count += 1
# print(count)

# checking  not vowels:

# vowel = ["a","e","i","o","u"]
# word = "josemarie"
# count = 0
# for i in word:
#     if i not in vowel:
#         count += 1
# print(count)

# occurence:

# word = "josemarie"
# ch = "e"
# count = 0
# for i in word:
#     if i == ch :
#         count += 1
# print(count)

# fibnacci series:


# def fibonacci(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
# n = 6
# print(fibonacci(n))  


# maximum number:

# numberList = [15, 85, 35, 89, 125]

# maxNum = numberList[0]
# for num in numberList:
#     if maxNum < num:
#         maxNum = num
# print(maxNum)

# finding index
# def index(arr,tar):
#     for i in range(len(arr)):
#         if arr[i] == tar:
#             return i
#     return -1
    
# print(index([2, 3, 5, 7, 11, 13, 17, 19, 23, 29] , 13))

# max sub arr sum:
# def max_subarray_sum(arr):
#     max_sum = current_sum = arr[0]
#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum
# arr = list(map(int,input().split()))
# print(max_subarray_sum(arr)) 

# def bubble_sort(arr):

# arr = [64, 34, 25, 12, 22, 11, 90]
# arr.sort()
# print(arr)



