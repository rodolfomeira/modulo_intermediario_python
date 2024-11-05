LL = int(input('Digite a linha de calçados: '))
match LL:
    case 16:
        print('Bebê')
    case 23:
        print('Infantil feminino')
    case 25:
        print('Infantil masculino')
    case 29:
        print('Infantil esportivo')
    case 42:
        print('Masculino formal')
    case 43:
        print('Masculino casual')
    case 49:
        print('Masculino esportivo')
    case 52:
        print('Feminino formal salto baixo')
    case 53:
        print('Feminino formal salto alto')
    case 55:
        print('Feminino casual salto baixo')
    case 56:
        print('Feminino casual salto alto')
    case 59:
        print('Feminino esportivo')
    case _:
        print('Código fornecido é inválido')