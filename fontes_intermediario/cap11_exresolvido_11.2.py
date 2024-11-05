arq = open('saida_er_11.2.txt', 'w')       # abre o arquivo para gravação
A = float(input('Digite um real: '))
while A != 0:
    arq.write(f'{A:.3f}\n')               # grava uma linha do arquivo
    A = float(input('Digite um real: '))
arq.close()                               # fecha o arquivo
print('Fim do Programa')
