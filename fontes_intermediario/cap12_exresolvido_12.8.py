from time import sleep
def Contagem(Cont):
    if Cont == 0:
        print('NO AR!!!')
    else:
        print(Cont)
        sleep(1)           # faz uma pausa de 1 segundo no programa
        Contagem(Cont-1)

toques = int(input('Digite a quantidade de toques da contagem: '))
print(f'Atenção para o toque de {toques} segundos...')
Contagem(toques)
