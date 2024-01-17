####l = [0,1,2,3,4,5,6,7,8,9,10]
####even = []
####odd = []
####count = len(l)
####
####for i in range(count):
####    if l[i] % 2 == 0:
####        even.append(l[i])
####    else:
####        odd.append(l[i])
####
####
####print("even - ", even)
####print("odd - ", odd)
##
####list methods:
####
####1. append()
##
##l = [1,2,3,4,5]
##l.append(6)
##print(l)
##
####2.clear()
##
##l = [1,2,3,4,5]
##l.clear()
##print(l)
##
####3.copy()
##
##l = [1,2,3,4,5]
##l.copy()
##print(l)
##
##
####4.count()
##
##l = [1,3,2,3,4,3,5]
##l = l.count(3)
##print(l)
##
####5.extend()
##
##l = [1,2,3,4,5]
##x = [6,7,8]
##l.extend(x)
##print(l)
##
####6.index()
##
##l = [1,3,2,3,4,3,5]
##l = l.index(3)
##print(l)
##
####7.insert()
##
##l = [1,3,2,3,4,3,5]
##l.insert(1,6)
##print(l)
##
####8.pop()
##
##l = [1,3,2,3,4,3,5]
##l.pop(3)
##print(l)
##
####9.remove()
##
##l = [1,3,2,3,4,3,5]
##l.remove(2)
##print(l)
##
####10.reverse()
##
##l = [1,3,2,3,4,3,5]
##l.reverse()
##print(l)
##
####11.sort()
##
##l = ["josemarie","tressia","anto","veronica"]
##l.sort()
##print(l)
##l = [0,3,5]
##x = 0
##for i in range(1,3):
##    x = x + l[i]
##print("the sum : " , x)

##l = [0,3,0,5,8]
##x = 1
##for i in range () :
##    x = x * l[i]
##print("the sum : " , x)

l = [1,3,24,5,8]
print(l)
x = l[0]
for i in  l:
    if i < x:
        x = i
print("the smallest number : " , x)


l = [1,3,24,5,8]
print(l)
x = l[0]
for i in  l:
    if i > x:
        x = i
print("the largest number : " , x)









































