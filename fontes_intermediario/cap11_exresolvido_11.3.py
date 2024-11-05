Lst = []
A = float(input('Digite um real: '))
while A != 0:
    Lst.append(f'{A:.3f}\n')
    A = float(input('Digite um real: '))
arq = open('saida_er_11.3.txt', 'w')       # abre o arquivo para gravação
arq.writelines(Lst)                       # grava toda a lista em linhas do arquivo
arq.close()                               # fecha o arquivo
print('Fim do Programa')
