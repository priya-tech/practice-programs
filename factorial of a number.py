print("enter the number")
n=int(input())
fact=1
print("the factorial of a number {0} is ".format(n))
for i in range(1,n+1):
    fact=fact*i
print(fact)
