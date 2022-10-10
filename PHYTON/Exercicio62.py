primeiro = int(input('Qual é o seu termo ?'))
razao = int(input('Qual é sua razão ?'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <=total:
        print('{} --'.format(termo), end= '')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar ?'))
print ('FIM!')

