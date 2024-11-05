from random import randint
Qtde = int(input('Digite a quantidade: '))
conjunto = set()
while len(conjunto) < Qtde:
    conjunto.add(randint(1, 50))
print(conjunto)
print('Fim do Programa')
