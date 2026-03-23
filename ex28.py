precoatual=0
mediamensal=0
preconovo=0

precoatual=float(input("digite o valor do  preço atual do produto"))

mediamensal=float(input("digite a media mensal"))

if(mediamensal<500 and precoatual <30):
    preconovo=(precoatual*10/100)+precoatual
elif(mediamensal>=500 and precoatual>=30 and precoatual<80):
    preconovo=(precoatual*15/100)+precoatual
elif(mediamensal>=1000 and precoatual>=80):
    preconovo=-precoatual-(precoatual*5/100)
else:
    preconovo=precoatual
print("o preco novo e ",preconovo  )
