UF = {}
print('Leitura dos dados')
while True:
    sigla = input('  Digite a sigla: ')
    if sigla == '':
        break        # interrompe o laço se cod == ''
    elif sigla in UF:
        print(f'  ...o código {sigla} já está no cadastro')
        continue     # segue para a próxima iteração
    estado = input('  Digite o nome: ')
    capital = input('  Digite a capital: ')
    pib = float(input('  Digite o PIB: '))
    UF[sigla] = (estado, capital, pib)	# acrescenta novo item ao dicionário
print('Fim da leitura dos dados\n')

print('     {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados[0],
        dados[1],
        dados[2] )
    )
print("\nFim do programa")
