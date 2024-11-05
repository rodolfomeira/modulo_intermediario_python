def Operacoes(a, b):
    soma = a + b
    dife = a - b
    mult = a * b
    divi = a / b
    return soma, dife, mult, divi

v1 = float(input('Digite o valor 1: '))
v2 = float(input('Digite o valor 2: '))
resultados = Operacoes(v1, v2)
print('Resultados')
print(f'  soma = {resultados[0]:.2f}')
print(f'  diferença = {resultados[1]:.2f}')
print(f'  multiplicação = {resultados[2]:.2f}')
print(f'  divisão = {resultados[3]:.2f}')
