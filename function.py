##n = [0,1,2,3,4]
##def valueequaltoindex(arr):
##    for i in n[]:
##        print(arr[1])
##valueequaltoindex(n)
##n = [1,2,2,2,5,7,9]
##x = 2
##def count_of_elements(n):
##    count = 0
##    for i in n:
##        if x >= i:
##            count += 1
##    return count
##count = count_of_elements(n)
##print(count)
##n = 5
##def print_array(n):
##    for i in range(0,n):
##        print(i,end = " ")
##print_array(n)
def is_balanced_parentheses(s: str) -> bool:
    open_list = ["(", "{", "["]
    close_list = [")", "}", "]"]
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

