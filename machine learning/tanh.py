import math
import numpy as n
n.random.seed(1)
def tanh(x):
    return ((2/(1+n.exp(-2*x)))-1)
def bal(x):
    return(1-pow(tanh(x),2))
x=n.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y=n.array([[0, 1, 0, 1]]).T
find=n.array([1, 1, 0])
w=2*n.random.random((3, 1))-1
for i in range(10000):
    op=tanh(n.dot(x,w))
    err=y-op
    w=w+n.dot(x.T,err*bal(op))
ans=tanh(n.dot(find,w))
print(ans)
if(ans<0.5):
    print(0)
elif(ans==0.5):
    print("undecidable")
else:
    print(1)
