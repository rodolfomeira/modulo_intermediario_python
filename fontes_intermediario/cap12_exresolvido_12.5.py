def LeReal(pLMin, pLMax):
    a = float(input('Digite um valor real: '))   # lê o valor
    while a < pLMin or a > pLMax:  # permanece em laço enquanto o valor for inválido
        print(f'O valor {a} está fora dos limites [{pLMin}, {pLMax}]')
        a = float(input('Digite um valor real: '))
    return a  # quando o valor for válido retorna

LMin = float(input('Digite o valor mínimo: '))
LMax = float(input('Digite o valor máximo: '))
controle = 's'
while controle == 's' or controle == 'S':
    Valor = LeReal(LMin, LMax)
    print(f'O valor lido é {Valor}')
    controle = input('\nQuer digitar outro valor (s/n)? ')
print('Fim do Programa')