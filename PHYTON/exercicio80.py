valores = []

for c in range(0,5):
    n = (int(input('Digite um valor:')))
    if c == 0 or  n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('=='*50)
print(f'O valores digitados em ordem foram {valores} ')

