
def power(A,n,p):
    if n ==0:
        return 1
    elif n % 2 == 1:
        return (power(A,n-1,p)*A %p)
    root = power(A,n//2,p)
    return (root*root)%p

print(power(435456,17,1000000))
print(power(131072,28,1000000))