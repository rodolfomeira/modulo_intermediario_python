def calcElemento(lin, col):
    if col == 0 or col == lin:
        return 1
    else:
        return calcElemento(lin - 1, col - 1) + calcElemento(lin - 1, col)

def criaLinhas(qtdeLinhas):
    resultado = []
    for linha in range(qtdeLinhas):
        valores_linha = []
        for coluna in range(linha + 1):
            valores_linha.append(calcElemento(linha, coluna))
        resultado.append(valores_linha)
    return resultado

def ExibeTriangulo(T):
    S = []
    for linha in T:
        saida = ''
        for elemento in linha:
            saida = saida + ' ' + str(elemento)
#        saida = ' '.join([str(elemento) for elemento in linha])
        S.append(saida)
    largura = len(S[-1])
    for saida in S:
         print(f'{saida:^{largura}s}')


qtdeLinhas = int(input('Digite a quantidade: '))
TriangPascal = criaLinhas(qtdeLinhas)
ExibeTriangulo(TriangPascal)