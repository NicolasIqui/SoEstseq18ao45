base=0
expoente=0
resultado=0
base=int(input("digite o valor d abase"))
expoente=int(input("digite o valor do expoente"))
resultado=base
for i in range (1,expoente):
    resultado=base*resultado
print(resultado)
