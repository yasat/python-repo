x1=list()
x2=list()
w1=list()
w2=list()
y=list()
def ask(x1,x2,y):
    rx1=input("enter inputs 1 with spaces: ")
    x1=rx1.split(" ")
    rx2=input("enter inputs 1 with spaces: ")
    x2=rx2.split(" ")
    ry=input("enter outputs with spaces: ")
    y=ry.split(" ")
    if(len(x1)!=len(x2)):
        return(x1,x2,y)
    for i in range(len(x1)):
        x1[i]=int(x1[i])
        x2[i]=int(x2[i])
    for i in range(len(y)):
        y[i]=int(y[i])
    return(x1,x2,y)
x1,x2,y=ask(x1,x2,y)
while(len(x1)!=len(y) and len(x1)!=len(x2)):
    print("numbers vary. enter properly again")
    x1,x2,y=ask(x1,x2,y)
we=int(input("enter initial weight: "))
for i in range(len(x1)):
    w1.append(we)
    w2.append(we)
red=float(input("enter reduction: "))
ite=int(input("enter no of iterations: "))
for i in range(len(x1)):
    for j in range(ite*100):
        ny=x1[i]*w1[i]+x2[i]*w2[i]
        if(ny>y[i]):
            if(ny%y[i]==0):
                by=ny/y[i]
                w1[i]=w1[i]/by
                w2[i]=w2[i]/by
                continue
             ##logic to be found..   
avg_w1=(sum(w1)/len(w1))
avg_w2=(sum(w2)/len(w2))
ver=input("enter values to verify: ").split(" ")
ver[0]=int(ver[0])
ver[1]=int(ver[1])
ans=round(ver[0]*avg_w1+ver[1]*avg_w2)
print(ans)
