#declarar
n1=0
n2=0

#inicio
n1=float(input("digite o primeiro numero"))
n2=float(input("digite o segundo numero"))

if(n1>n2):
    if(n1%n2==0):
        print(n1,"e multiplo de ",n2)
    else:
         print(n1,"nao e multiplo de ",n2)
else:
    if(n2>n1):
        if(n2%n1==0):
            print(n2,"e multiplo de ",n1)
        else:
            print(n2," nao e multiplo de ",n1)
    else:   
        print("os numeros sao iguais")