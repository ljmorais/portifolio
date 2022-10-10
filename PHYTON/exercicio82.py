lista = []
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um numero:')))
    r = str(input('Você quer continuar ? [S/N]'))
    if r in 'Nn':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)

print('=='*30)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')