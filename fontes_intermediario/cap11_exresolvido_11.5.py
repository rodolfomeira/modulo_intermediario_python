Lst = []
for linha in open('entrada_er_11.4.txt'):   # abre o arquivo e o usa como iterável - 'r' foi omitido
    Lst.append(int(linha))                 # converte linha para inteiro e coloca na lista
print('Valores lidos do arquivo')
print(Lst)
Soma = sum(Lst)    # calcula a soma dos elementos da lista
print(f'Soma dos valores = {Soma}')
Qtde = len(Lst)    # determina a quantidade dos elementos da lista
print(f'Quantidade = {Qtde}')
print(f'Média dos valores = {Soma/Qtde}')
Minimo = min(Lst)  # determina o menor elemento da lista
print(f'Mínimo dos valores = {Minimo}')
Maximo = max(Lst)  # determina o maior elemento da lista
print(f'Máximo dos valores = {Maximo}')
print('Fim do Programa')

