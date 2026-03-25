n1=0
maior=0
menor=0

for i in range (100):
    n1=int(input("digite um valor"))
    if i == 0:
        maior = n1
        menor = n1
    if (n1>=maior):
        maior=n1
    elif(n1<menor):
        menor=n1
    
    print(maior,menor)

print(maior,menor)
