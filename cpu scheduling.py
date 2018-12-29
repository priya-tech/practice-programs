def findwaitingtime(n,bt,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i]=bt[i-1]+wt[i-1]
def turnaroundtime(n,bt,wt,tat):
     for i in range(0,n):
        tat[i]=bt[i]+wt[i]
        
def findavgtime(n,bt):
    wt=[0]*n
    tat=[0]*n
    tot_wt=0
    tot_tat=0
    findwaitingtime(n,bt,wt)
    turnaroundtime(n,bt,wt,tat)
    print("processes","   ","burst time","    ","waititng time","   ","turnaroundtime")
    for i in range(0,n):
        print("  ",i+1,"  \t\t  ",bt[i]," \t\t   ",wt[i],"\t\t",tat[i])
        tot_wt=tot_wt+wt[i]
        tot_tat=tot_tat+tat[i]
    avg_wt=float(tot_wt)/float(n)
    avg_tat=float(tot_tat)/float(n)
    print("average waiting time",avg_wt)
    print("average turn around time",avg_tat)
print("enter the no. of processes")
n=int(input())
bt=[0]*n
for i in range(0,n):
    print("enter the burst time for processor %d"%(i+1))
    bt[i]=int(input())
    
findavgtime(n,bt)    
