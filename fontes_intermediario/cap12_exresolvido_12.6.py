def CalculaMedia(pNotas):
    '''Recebe o string pNotas, faz a separação dos valores, calcula e retorna a média'''
    pNotas = pNotas.split()          # o objeto pNotas recebido também será usado como retorno da função
    for i in range(len(pNotas)):     # converte as notas lidas para float
        pNotas[i] = float(pNotas[i])
    media = pNotas[0] * 0.3 + pNotas[1] * 0.3 + pNotas[2] * 0.3 + pNotas[3] * 0.1
    situacao = 'APROVADO' if media >= 7 else 'REPROVADO'
    pNotas.append(media)             # acrescenta media na lista de retorno
    pNotas.append(situacao)          # acrescenta situacao na lista de retorno
    return pNotas

notas = input('Digite 4 notas (P1 P2 P3 NT): ')
resultado = CalculaMedia(notas) # chama a função passando o string lido e retornando uma lista com resultados
print(f'P1 = {resultado[0]:.1f}; ', end='')
print(f'P2 = {resultado[1]:.1f}; ', end='')
print(f'P3 = {resultado[2]:.1f}; ', end='')
print(f'NT = {resultado[3]:.1f} -> ', end='')
print(f'Média = {resultado[4]:.1f} ', end='')
print(f'Situação: {resultado[5]}')
