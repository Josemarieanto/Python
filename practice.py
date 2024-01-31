##n = 5
##def seriessum(n):
##    seriessum = 0
##    for i in range(1,n+1):
##        seriessum += i
##    return seriessum
##result = seriessum(n)
##print(result)
l = [1, 2, 3, 4, 5]
def print_alternate_elements(arr):
    for i in range(0, len(arr), 2):
        print(arr[i],end = "  ")
print_alternate_elements(l)

