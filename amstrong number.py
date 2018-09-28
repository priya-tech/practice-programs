n=int(input("enter the number"))
a=n
num=n
y=1;x=0;count=0;sum=0
while num!=0:
    num=int(num/10)
    count=count+1
    
while a!=0:
    x=a%10
    for i in range(1,count+1):
        y=y*x
    sum=sum+y    
    a=int(a/10)
    y=1
if sum==n:
    print("its amstrong number")
else:
    print("its not a amstrong number")
    
