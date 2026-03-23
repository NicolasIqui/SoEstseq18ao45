tipoinvi=0
valorinvi=0

tipoinvi=int(input("digite o tipo do investimento (1 = poupança e 2 = renda fixa) "))
valorinvi=float(input("digite o valor do investimento"))

if(tipoinvi==1):
    valorinvi=(valorinvi*3/100)+valorinvi
elif(tipoinvi==2):
        valorinvi=(valorinvi*5/100)+valorinvi
else:
      print("tipo da conta invalida")
print("o valor do sue investimento esta atualmente em ",valorinvi )