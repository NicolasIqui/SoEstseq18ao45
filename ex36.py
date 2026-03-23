fat=1
n=0
n=int(input("digite um valor de um numero "))
serie=1
i1=0
for i in range(1, n+1):
    fat=fat*i
    i1=fat
    serie=serie+(1/i1)
print(f"resultado da serie {serie}")



