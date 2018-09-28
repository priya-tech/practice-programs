print("enter the number to check")
n=int(input())
f=0
for i in range(0,n):
    a=i*i
    if a==n:
        f=1
        break
if f==1:
    print("its a perfect square")
else:    
    print("its not a perfect square")


