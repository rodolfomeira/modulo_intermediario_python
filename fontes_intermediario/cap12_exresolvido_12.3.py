def Divisivel(A, B):
    return True if A % B == 0 else False

valorA = int(input('Digite A: '))
valorB = int(input('Digite B: '))
if Divisivel(valorA, valorB):
    print(f'{valorA} é divisível por {valorB}')
else:
    print(f'{valorA} não é divisível por {valorB}')
