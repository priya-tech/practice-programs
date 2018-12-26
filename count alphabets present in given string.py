def count(name):
    for i in name:
        count=0
        for j in name:
            if i==j:
                count=count+1
        print("%s present %d times"%(i,count))        
print("enter the string to count alphabets")                
name=input()
count(name)
