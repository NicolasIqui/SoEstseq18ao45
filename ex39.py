total = 0
graos = 1

for casa in range(1, 65):
    total = total + graos
    print(f"Casa {casa}: {graos} grãos")
    graos = graos * 2

print("Total de grãos:", total)