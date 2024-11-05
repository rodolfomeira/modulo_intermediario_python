Estoque = {}
for linha in open('entrada_er_11.6.txt'):   #
    lst = linha.rstrip().split(';')
    cod = int(lst[0])
    qtde = int(lst[1])
    pcunit = float(lst[2])
    Estoque[cod] = (qtde, pcunit)
print('Valores carregados no dicionário')
print(Estoque)
print('\nExibição dos dados na forma de tabela')
TotGeral = 0
for cod, dados in Estoque.items():
    tot = dados[0] * dados[1]
    TotGeral += tot
    print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}')
print(' ' * 24, f'{TotGeral:8.2f}')
print('\nFim do Programa')