n=0
n=int(input("digite um valor de um numero "))
serie=1
for i in range(1, n+1):
    print(serie)

    serie=serie+(1/i)
print(f"resultado da serie {serie}")