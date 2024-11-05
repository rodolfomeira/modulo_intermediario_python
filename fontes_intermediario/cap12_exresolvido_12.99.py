def CalculaMedia(pNotas):
    '''Recebe o string pNotas, faz a separação dos valores, calcula e retorna a média'''
    pNotas = pNotas.split()
    for i in range(len(pNotas)):
        pNotas[i] = float(pNotas[i])
    pNotas.append(pNotas[0] * 0.4 + pNotas[1] * 0.4 + pNotas[2] * 0.2)
    return pNotas

def ExibeResultado(pNotas):
    '''Recebe a lista pNotas e produz a saída especificada'''
    print(f'  n1 = {pNotas[0]:.1f}; ', end='')
    print(f'n2 = {pNotas[1]:.1f}; ', end='')
    print(f'nt = {pNotas[2]:.1f} -> ', end='')
    print(f'Média = {pNotas[3]:.1f} ')

notas = input('Digite as três notas: ')
while notas != '':
    notas = CalculaMedia(notas)
    ExibeResultado(notas)
    notas = input('Digite as três notas: ')
print('\nFim do Programa')