#declarar
n1=0
n2=0
n3=0
n4=0
#inicio
n1=float(input("digite o primeiro numero"))
n2=float(input("digite o segundo numero"))
n3=float(input("digite o terceiro numero"))
n4=float(input("digite o quarto numero"))

if(n4<n1):
    print(n4,n1,n2,n3,)
elif(n4<n2):    
    print(n1,n4,n2,n3)
elif(n4<n3):
    print(n1,n2,n4,n3)
else:
    print(n1,n2,n3,n4)        