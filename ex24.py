n1=0

n1=int(input("digite um numero "))

if(n1%2==0 and n1%3==0):
    print("e divisivel por 2 e por 3")
elif(n1%2==0):
    print("so e divisivel por 2")
elif(n1%3==0):
    print("so e divisivel por 3")
else:
    print("nao e divisivel por nenhum dos dois")