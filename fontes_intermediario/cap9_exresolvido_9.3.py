from random import randint
Qtde = int(input('Digite a quantidade: '))
Lista = []
for i in range(Qtde):
    Lista.append(randint(1, 50))
print('\nLista gerada:')
print(Lista)
conjunto = set(Lista)  # converte a lista em conjunto
Lista = set(conjunto)  # retorna o conjunto para lista
print('\nLista com valores não repetidos:')
print(Lista)
print(f'A nova lista tem {len(conjunto)} elementos')
print('Fim do Programa')