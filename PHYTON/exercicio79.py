lista = []

while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, nao pode ser adicionado.')
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break

print ('---'*50)
lista.sort()
print(f'Você adicionou os valores {lista}')