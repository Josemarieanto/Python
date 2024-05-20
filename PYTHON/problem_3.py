def prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return n,"is not a prime"
        return n,"is a prime"

n = int(input())
print(prime(n)) 

# here the function checks whether it is a prime number or not.
# if input ,n provided is divisble by i ,then it is not a prime number.
# if it is not divisible it is a prime number


