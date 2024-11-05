produtos = {}
print('Leitura dos dados')
cod = input('  Digite o código: ')
while cod != '':
    preco = float(input('  Digite o preço: '))
    produtos[cod] = preco	# acrescenta novo item ao dicionário
    cod = input('  Digite o código: ')
print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():
    print(f'  produto {cod} custa R$ {produtos[cod]:7.2f}')
print("\nFim do programa")
