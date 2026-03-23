n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 < n2:
    for i in range(n1 + 1, n2):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
elif n2 < n1:
    for i in range(n2 + 1, n1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
else:
    print("Não há números entre eles, são iguais.")