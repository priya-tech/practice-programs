print("enter the numbers to find gcd")
m=int(input())
n=int(input())
def gcd(x,y):
    while(y):
        x,y=y,x%y
    gcd=x
    return gcd
print("GCD of {0} and {1} is ".format(m,n))
print(gcd(m,n))

