Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if clássico')
for codigo in Codigos:
    if codigo >= 120 and codigo <= 200:
        Lista.append(codigo)
print(f'  códigos filtrados -> {Lista}')

print('\nAlternativa com if de única linha')
Lista = []
for codigo in Codigos:
    Lista.append(codigo) if codigo >= 120 and codigo <= 200 else 0
print(f'  códigos filtrados -> {Lista}')
