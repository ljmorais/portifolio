listagem = ('Lapis', 1.75,
           'Borrcha', 0.50,
           'Caneta', 1.00,
           'Livro', 40.00,
           'Mochila', 65.00)

print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)

