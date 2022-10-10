valores = []
mai = 0
men = 0
for c in range( 0,5):
    valores.append(int(input(f'Digite um valor para posição {c}:')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print(f'a lista dos valores é {valores}')
print(f'O maior valor encontrado na lista foi {mai} na posição', end= ' ')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}', end='')
print()
print(f'O menor valor encontrado na lista foi {men} na posição', end= ' ')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}', end='')
print()