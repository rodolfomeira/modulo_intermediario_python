def Paridade(a):
    if a % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

n = int(input('Digite um inteiro: '))
print(Paridade(n))

