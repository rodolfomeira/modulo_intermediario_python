from random import randint
def CarregaLista(qtde, a, b):
    L = []
    for i in range(qtde):
        L.append(randint(a, b))
    return L

q = int(input('Digite a quantidade desejada: '))
lmin = int(input('Digite o limite mínimo: '))
lmax = int(input('Digite o limite máximo: '))
valores = CarregaLista(q, lmin, lmax)
print(f'Lista gerada >> {valores}')
print(f'A lista gerada tem {len(valores)} elementos')
