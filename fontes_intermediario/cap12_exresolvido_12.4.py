def CalcDigito(cod):
    s = str(cod)    # transforma o código em string para usar como iterador
    peso = 2
    dv = 0
    for a in s:     # processa cada algarismo em s
        dv += peso * int(a)   # converte o algarismo para int, multiplica pelo peso e acumula
        peso += 1   # incrementa o peso
    return dv % 7

codigo = int(input('Digite o código: '))
while codigo > 0:
    digito = CalcDigito(codigo)
    print(f'Código: {codigo} -> dígito: {digito}')
    codigo = int(input('Digite o código: '))
print('\nFim do Programa')
