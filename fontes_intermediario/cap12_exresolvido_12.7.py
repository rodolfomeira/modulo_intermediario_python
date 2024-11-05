def Primo(V):
    '''Se V for primo retorna True, senão retorna False'''
    if V == 2:        # V é ímpar
        return True
    elif V % 2 == 0:  # V é par maior que 2
        return False
    else:             # testa se V ímpar é primo
        raiz = pow(V, 0.5) # a raiz de V é o limite dos testes necessários
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False # se for divisível retorna falso imediatamente
            i += 2
        return True # se chegar no final do laço então é primo

N = int(input('Digite um inteiro: '))
if Primo(N):
    print(f'{N} é primo')
else:
    print(f'{N} não é primo')