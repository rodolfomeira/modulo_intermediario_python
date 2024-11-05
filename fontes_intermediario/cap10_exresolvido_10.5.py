Alunos = {}
Q = int(input('Digite a qtde de alunos: '))
for i in range(Q):
    nome = input(f'  nome do aluno {i+1} >> ')
    notas = input(f'  notas do {nome} >> ')
    notas = notas.split()
    for j in range(len(notas)):
        notas[j] = float(notas[j])
    Alunos[nome] = tuple(notas)

print('\nResultado da Turma')
for nome, notas in Alunos.items():
    media = sum(notas)/len(notas)
    if media >= 6.0:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    print('{:12} {:4.1f} {:4.1f} {:4.1f} {:4.1f} {} com média = {:4.1f}'.format(
        nome,
        notas[0],
        notas[1],
        notas[2],
        notas[3],
        situacao,
        media)
    )
print('Fim do Programa')