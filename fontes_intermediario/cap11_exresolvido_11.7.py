codGravacao = input('Digite a codificação de Gravação: ')
codLeitura = input('Digite a codificação de Leitura: ')

print('Etapa de gravação do arquivo')
arq = open('codificacao.txt', 'w', encoding=codGravacao)
arq.write('Gravação de Arquivo\n')
arq.write('acentos: á, é, í, Á, É, Í, ç, Ç\n')
arq.close()

print('\nEtapa de leitura do arquivo')
arq = open('codificacao.txt', 'r', encoding=codLeitura)
s = arq.readline()
print(s.rstrip())
s = arq.readline()
print(s.rstrip())
arq.close()

print('Fim do Programa')
