def soma(P, R, Q):
    '''P: primeiro termo - R: razão - Q: quantidade'''
    if Q > 0:
        a = P + soma(P+R, R, Q-1)
        return a
    else:
        return 0

Prim = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a razão: '))
Qtde = int(input('Digite a quantidade: '))
Resultado = soma(Prim, Razao, Qtde)
print(f'para Prim = {Prim}; Razao = {Razao}; Qtde = {Qtde} -> Soma = {Resultado}')
