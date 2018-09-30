print("enter the two numbers to find gcd")
m=int(input())
n=int(input())
if m>n:
    smaller=n
else:
    smaller=m
def gcd(x,y):
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
print("GCD of {0} and {1} is".format(m,n))
print(gcd(m,n))
