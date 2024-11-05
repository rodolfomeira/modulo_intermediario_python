arq = open('saida_er_11.1.txt', 'w')       # abre o arquivo para gravação
A = int(input('Digite um inteiro: '))
while A != 0:
    arq.write(f'{A}\n')                   # grava uma linha do arquivo
    A = int(input('Digite um inteiro: '))
arq.close()                               # fecha o arquivo
print('Fim do Programa')
