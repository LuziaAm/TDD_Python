x = 0
y = 0
z = 0
direcao = ['Norte', 'Sul', 'Lest', 'Oeste']

# posicaoInicio = []

print('---Digite os comandos---')
x = input('Digite o valor de X: ')
y = input('Digite o valor de Y: ')
z = input('Digite o valor de Z: ')


if (x == 0 and y == 0 and z == 0):
    posicaoInicio = x, y ,z
    print('Posicao Inicial', posicaoInicio)
    print(direcao[0])   

else:
    print(x, y, z)


