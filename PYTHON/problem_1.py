def two_sums(n,t):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]+n[j] == t:
                return i, j

l = list(map(int,input().split()))
t = int(input())
print(two_sums(l,t))

# here, the function takes two parameters.
# n represents the list of elements and t represents the target.
# the function will iterate over the items and returns the indices of the element that achieve the targeted output.