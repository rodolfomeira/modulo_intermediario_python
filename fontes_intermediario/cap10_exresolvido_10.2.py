produtos = {}
print('Leitura dos dados')
while True:
    cod = input('  Digite o código: ')
    if cod == '':
        break        # interrompe o laço se cod == ''
    elif cod in produtos:
        print(f'  ...o código {cod} já está no cadastro')
        continue     # segue para a próxima iteração
    preco = float(input('  Digite o preço: '))
    produtos[cod] = preco	# acrescenta novo item ao dicionário
print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():
    print(f'  produto {cod} custa {produtos[cod]}')
print("\nFim do programa")
