import math
a=0
b=0
c=0
delta=0
x1=0
x2=0

#inicio
a=float(input("digite  o valor de a"))
b=float(input("digite  o valor de b"))
c=float(input("digite  o valor de c"))
delta=b*b-(4*a*c)

if(delta>0):
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("x1 =" ,x1)
    print("x2 =" ,x2)
elif(delta<0):
    print("naoe xiste raizes reais")
else:
    x1=(-b)/(2*a)
    print("x1 =" ,x1)

