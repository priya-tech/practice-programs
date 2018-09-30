print("enter the numbers to find lcm")
m=int(input())
n=int(input())
def lcm(x,y):
    if m>n:
        greater=m
    else:
        greater=n

    while(True):
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
print("LCM of {0} and {1} is".format(m,n))
print(lcm(m,n))
    

    
