n=int(input("enter the number to check"))
count=0
while n!=0:
    n=int(n/10)
    count=count+1
print("the number of digits in the number is",count)    
