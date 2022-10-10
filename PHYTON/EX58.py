from random import randint
computador = randint(0,10)
print ('Ola, sou o seu computador e acabei de pensa em um numero de 0 a 10.')
print('Será que você consegue advinhar, qual foi....')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu numero escolhido ?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais')
        elif jogador > computador:
            print ('Menos')
print('Acertou!')
print('Você tentou {} vezes para acertar o numero'.format(palpites))

