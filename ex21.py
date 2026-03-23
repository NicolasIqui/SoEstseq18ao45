#declarar
n1=0
n2=0
n3=0
n4=0
media=0
#inicio
n1=float(input("digite a primeira nota"))
n2=float(input("digite a segunda nota"))
n3=float(input("digite a terceira nota"))
n4=float(input("digite a quarta nota"))
media=(n1+n2+n3+n4)/4
if(media>=6):
    print("aprovado")
elif(media>=3):
    print("exame")
else:
    print("retido")     