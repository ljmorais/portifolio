cont = ('zero','um','dois', 'tres','quatro','cinco',
        'seis', 'sete' , 'oito', 'nove' ,'dez','onze',
        'doze','treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete','dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero de 0 á 20:'))
    if 0<= num <= 20:
        break
    print('TENTE NOVAMENTE.', end=' ')

print(f'O numero que você digitou o numero {cont[num]}')

perg = ' '
while perg not in 'SN':
    perg = str(input('Você quer continuar ? [S/N] ')).strip().upper()[0]

    if perg == 'S':
        num = int(input('Digite um numero de 0 á 20:'))
        print(f'O numero que você digitou o numero {cont[num]}')

    else:
        print('O JOGO FOI FINALIZADO')
        break

