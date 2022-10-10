lista = []

while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
    r = str(input('Quer Continuar [S/N] ? '))
    if r in 'Nn':
        break
print('==='*50)

print(f'Foram digitados {len(lista)} numeros na lista')

print('==='*50)
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica {lista}')

print('==='*50)

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não se encontra na lista')

