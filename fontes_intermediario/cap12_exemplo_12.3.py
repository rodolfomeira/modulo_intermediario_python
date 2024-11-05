from random import randint
def CarregaLista():
    L = []
    for i in range(10):
        L.append(randint(1, 1000))
    return L

valores = CarregaLista()
print(f'Lista gerada >> {valores}')