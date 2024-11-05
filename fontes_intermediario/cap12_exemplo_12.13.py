def funcao1():
    print('dentro da função1 temos >>', a, b)

def funcao2():
    global a  # nesta linha informamos que a é o objeto global
    a = 100   # nesta linha estamos alterando o valor do a global
    b = 200   # nesta linha estamos criando um objeto local b
    print('dentro da função2 temos >>', a, b)

a = 10
b = 20
funcao1()
funcao2()
print('fora da função temos >>', a, b)