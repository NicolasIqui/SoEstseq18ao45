serie = 0

for i in range(1, 16):
    if i == 1:
        serie =serie+1  
        print(f"serie  {serie}")
    elif i % 2 == 0:
        print(f"{serie} - {i}/({i*i})")
        serie =serie- i / (i * i)
    else:
        print(f"{serie} + {i}/({i*i})")
        serie =serie+i / (i * i)
print(serie)