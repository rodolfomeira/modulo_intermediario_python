def funcao1():
    print('dentro da função1 temos >>', a, b)

def funcao2():
    global a
    a = 100
    b = 200
    print('dentro da função2 temos >>', a, b)

a = 10
b = 20
funcao1()
funcao2()
print('fora da função temos >>', a, b)