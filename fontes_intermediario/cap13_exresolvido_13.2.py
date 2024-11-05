Precos = []
print('Forneça os preços para a lista. Zero para terminar.')
preco = float(input('  digite um valor real: '))
while preco != 0:
    Precos.append(preco)
    preco = float(input('  digite um valor real: '))
print('Os preços são estes:')
print(Precos)

aumento = float(input('Digite a porcentagem de aumento (sem o %): '))
# este list comprehension aplica o aumento
#NovosPrecos = [valor * (1+aumento/100) for valor in Precos if valor < 100]
NovosPrecos = [valor * (1+aumento/100) if valor < 100 else valor for valor in Precos]
# exibição do resultado, um valor por linha
for valor in NovosPrecos:
    print(f'{valor:.2f}')