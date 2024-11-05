n = -1
while n != 0:
    n = int(input('Digite um inteiro: '))
    match n:
        case 1:
            print('  você digitou um')
        case 2:
            print('  você digitou dois')
        case 3:
            print('  você digitou três')
        case _:
            print('  você digitou outra coisa')
print('Fim do Programa')
