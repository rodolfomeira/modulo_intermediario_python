from random import randint
def CarregaLista(qtde):
    L = []
    for i in range(qtde):
        L.append(randint(1, 1000))
    return L

q = int(input('Digite a quantidade desejada: '))
valores = CarregaLista(q)
print(f'Lista gerada >> {valores}')
print(f'A lista gerada tem {len(valores)} elementos')
