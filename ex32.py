n=0
n1=0
resultado=0
fat=1

n = int(input("Digite um  numero "))
n1=n
for n1 in range (n1,1,-1):
    fat=n1*fat

print(f"o valor do fatorial de {n} =",fat) 

