n=int(input("enter the number to check"))
f=0
for i in range(2,n-1):
    if n%i==0:
        f=1
        break
if f==1:
    print("its not a prime number")
else:
    print("its a prime number")
    
