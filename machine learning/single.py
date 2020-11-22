x=list()
y=list()
w=list()
def ask(x,y):
    rx=input("enter inputs with spaces: ")
    x=rx.split(" ")
    ry=input("enter outputs with spaces: ")
    y=ry.split(" ")
    for i in range(len(x)):
        x[i]=int(x[i])
    for i in range(len(y)):
        y[i]=int(y[i])
    return(x,y)
def train(x,ite,w,y,bias,red):
    for i in range(len(x)):
        for j in range(int(ite*(1/red))):
            ny=x[i]*w[i]+bias
            if(ny>y[i]):
                w[i]=w[i]-red
            elif(ny<y[i]):
                w[i]=w[i]+red
            else:
                break
    return(w)
def test(x,w,y,bias):
    for i in range(len(x)):
        if(y[i]==round(x[i]*w+bias,5)):
            continue
        else:
            return(0)
    return(1)
def full():
    x=list()
    y=list()
    w=list()
    x,y=ask(x,y)
    while(len(x)!=len(y)):
        print("numbers vary. enter properly again")
        x,y=ask(x,y)
    we=int(input("enter initial weight: "))
    for i in range(len(x)):
        w.append(we)
    red=float(input("enter reduction: "))
    ite=int(input("enter no of iterations: "))
    bias=-red
    print("analysing data")
    print("=======================================================================")
    print("inputs: "+str(x))
    print("outputs: "+str(y))
    ret=0
    for z in range(int(ite*(1/red))):
        if(ret==0):
            bias=bias+red
            nw=train(x,ite,w,y,bias,red)
            avg_w=(sum(nw))/len(nw)
            ret=test(x,avg_w,y,bias)
        else:
            break
    if(ret==0):
        bias=red
        for z in range(ite*(1/red)):
            if(ret==0):
                bias=bias-red
                nw=train(x,ite,w,y,bias,red)
                avg_w=(sum(nw))/len(nw)
                ret=test(x,avg_w,y,bias)
            else:
                break
    print("weight: "+str(avg_w))
    print("bias: "+str(bias))
    print("iterations: "+str(ite))
    print("redution factor: "+str(red))
    print("=======================================================================")
    ver=int(input("enter value to verify: "))
    ans=round(ver*avg_w+bias)
    print(ans)
def train_test(x,y,ver,we=1,red=0.01,ite=10000,bias=-60.60):
    flag=0
    if(bias==-60.60):
        bias=-red
    tbias=bias
    while(len(x)!=len(y)):
        print("numbers vary. enter properly again")
        return(-1)
    for i in range(len(x)):
        w.append(we)
    print("analysing data")
    print("=======================================================================")
    print("inputs: "+str(x))
    print("outputs: "+str(y))
    ret=0
    for z in range(int(ite*(1/red))):
        if(ret==0):
            tbias=tbias+red
            nw=train(x,ite,w,y,tbias,red)
            avg_w=(sum(nw))/len(nw)
            ret=test(x,avg_w,y,tbias)
        else:
            break
    if(ret==0):
        flag=1
        bias=bias+red
        for z in range(ite*(1/red)):
            if(ret==0):
                bias=bias-red
                nw=train(x,ite,w,y,bias,red)
                avg_w=(sum(nw))/len(nw)
                ret=test(x,avg_w,y,bias)
            else:
                break
    print("weight: "+str(avg_w))
    if(flag==1):
        print("bias: "+str(bias))
    else:
        print("bias: "+str(tbias))
    print("iterations: "+str(ite))
    print("redution factor: "+str(red))
    print("=======================================================================")
    for i in range(len(ver)):
        if(flag==1):
            ans=round(ver[i]*avg_w+bias)
        else:
            ans=round(ver[i]*avg_w+tbias)
        print(str(ver[i])+": "+str(ans))
