x=input("enter the string to check")
len=0
rev=""
for i in x:
    len=len+1
while len>0:
    rev+=x[len-1]
    len=len-1
if x==rev:
    print("its a palindrome")
else:
    print("its not a palindrome")
