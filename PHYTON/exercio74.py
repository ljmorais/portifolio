from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os valores sorteado foi :')
for n in numeros:
    print(f'{n}', end= ' ')


print(('-='*50))

print(f'O maior valor sorteado foi {max(numeros)}')

print(('-='*50))

print(f'O menor valor sorteado foi {min(numeros)}')