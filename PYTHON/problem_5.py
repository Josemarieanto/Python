def sum13(nums):
   sum = 0
   for i in range (len(nums)):
      if nums[i] != 13:
        sum += nums[i]
      elif nums[i] == 13 and i < len(nums)-1:
         nums[i]=0
         nums[i+1] =0
   return sum

num = list(map(int,input().split()))
print(sum13(num))

#  here the loop will iterate over the elements in the list.
# if the list doesnt have the item 13, then it will sum up all teh element.
# if it contains 13, it will stop iterating over the items, and return the sum 
# upto the element 13.