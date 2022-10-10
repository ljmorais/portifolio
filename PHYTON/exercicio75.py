n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um outro numero:'))
n3 = int(input('Digite mais um numero:'))
n4 = int(input('Digite o ultimo numero:'))

numeros =(n1, n2 , n3 , n4)

print(f'Você digitou os valores {numeros}')

print('-='* 50)

print(f'o Valor 9 apareceu {numeros.count(9)} vezes')

print('-='* 50)
if 3 in numeros:
    print(f'Em qual posição foi digitado o valor 3: {numeros.index(3)} posição ')
else:
    print('O valor 3 não foi digitado em nenhum dos casos.')
print('-='* 50)

print(' Os valores pares digitado foram:' , end=' ')

for n in numeros:
    if n % 2 == 0:
        print(n,end= ' ')