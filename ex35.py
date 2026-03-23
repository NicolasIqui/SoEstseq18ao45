n1=0
n2=0
somatoria=0

n1=int(input("digite o primeiro numero "))
n2=int(input("digite o segundo numero "))
if(n1>n2):
    for i in range (n2+1,n1,):
        if(i%2!=0):
            somatoria=somatoria+i
    print(f" o maior entre eles e {n1} e a somatoria e = {somatoria}")
else:
    for i in range (n1+1,n2,):
        if(i%2!=0):
            somatoria=somatoria+i
    print(f" o maior entre eles e {n2} e a somatoria e = {somatoria}")