def GeraDados():
    '''Esta função inicializa 7 objetos de diferentes classes e os retorna'''
    a = 16
    b = 39.7
    c = 'texto'
    d = [1, 2, 3, 4]
    e = (0, 1)
    f = {80, 90, 100}
    g = frozenset((3, 4, 5))
    return a, b, c, d, e, f, g
    # Este retorno equivale a uma tupla. É o mesmo que (a, b, c, d, e, f, g)

Dados = GeraDados()
print('Relação de elementos gerados na função')
for x in Dados:
    print(f'{x} é objeto da classe {type(x)}')