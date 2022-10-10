
n1 = int(input('Qual é o seu primeiro numero ?'))
n2 = int(input('Qual é o seu segundo numero ?'))
opcao = 0
opcao != 5

print("[1] SOMAR"
      "[2] MULTIPLICAR"
      "[3] MAIOR"
      "[4] NOVOS"
      "[5] SAIR DO PROGRAMA")

opcao = int(input("Qual é a sua opção ?"))

if opcao == 1:
      soma = n1+n2
      print ('A soma entre os valores {} + {} é {}'.format(n1, n2, soma))
elif opcao ==2:
      produto = n1 * n2
      print ('A multiplicação dos valores {} * {} é {}'.format(n1, n2, produto))
elif opcao ==3:
      if n1>n2:
            maior = n1
      else:
            maior = n2
elif opcao == 4:
      print ('Informe os numeros novamente...')
      n1 = int(input('Primeiro valor ?'))
      n2 = int(input('Segundo valor ?'))
elif opcao ==5:
      print ('Finalizando')
else:
      print ('Opção invalida, tente novamente.')
print ('Fim do programa tente novamente')
