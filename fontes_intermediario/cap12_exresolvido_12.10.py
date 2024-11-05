def BuscaBin(valor, lista, ini, fim):
    '''Procura valor em lista, entre as posições ini:fim'''
    if ini > fim:
        return False
    meio = (ini + fim) // 2
    if valor == lista[meio]:
        return True
    elif valor < lista[meio]:
        return BuscaBin(valor, lista, ini, meio-1)
    else:
        return BuscaBin(valor, lista, meio+1, fim)

L = [14, 17, 20, 22, 23, 25, 28, 29, 31, 35, 40, 45, 50, 53, 56, 59, 62, 65]
X = int(input('Digite um valor para pesquisa na lista: '))
while X != 0:
    Achou = BuscaBin(X, L, 0, len(L)-1)
    if Achou != 0:
        # chamada para verificar a metade esquerda da lista
        print(f'{X} está na lista')
    else:
        # chamada para verificar a metade direita da lista
        print(f'{X} não está na lista')
    X = int(input('Digite um valor para pesquisa na lista: '))
print('Fim do Programa')
