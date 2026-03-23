nv=0
tempd=0
excir=0
velocidademe=0
dt=0
#inicio
nv=int(input("digite a quantidade de voltas"))
tempd=int(input("digite o tempo entre as voltas"))
excir=int(input("digite o tamanho do circuito"))

velocidademe=(nv*excir*60)/(1000*tempd)
print(velocidademe) 