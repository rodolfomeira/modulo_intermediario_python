def Fatorial(N):
    if N <= 1:
        return 1
    else:
        return N * Fatorial(N-1) # preste muita atenção a essa linha

Entrada = int(input('Digite um inteiro: '))
F = Fatorial(Entrada)
print(f'O fatorial de {Entrada} é {F}')