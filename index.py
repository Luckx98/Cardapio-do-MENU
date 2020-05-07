#coding: utf-8

from os import system
from time import sleep

n = 0

valorTotal = 0

def opcao1(valorTotal):
    opcaoHamburguer = 0
    while opcaoHamburguer !=4:
        print('''====== Hamburguers=======\n
        [ 1 ] R$10,90 - X-bacon\n
        [ 2 ] R$11,90 - X-salada\n
        [ 3 ] R$12,90 - X-bacon duplo\n
        [ 4 ] Voltar\n''')

        opcaoHamburguer = int(input('>>>>>>>>>>>> Digite uma opção: '))

        if opcaoHamburguer == 1:
            valorTotal += 10.90
            print('X-bacon adicionado com sucesso!')
            sleep(2)
            system('cls')
        elif opcaoHamburguer == 2:
            valorTotal += 11.90
            print('X-salada adicionado com sucesso!')
            sleep(2)
            system('cls')
        elif opcaoHamburguer == 3:
            valorTotal += 12.90
            print('X-bacon duplo adicionado com sucesso!')
            sleep(2)
            system('cls')
        elif opcaoHamburguer == 4:
            print('Voltando . . .')
            sleep(2)
            system('cls')
        else:
            print('Opção inválida! Digite novamente!')
            sleep(2)
            system('cls')
    return valorTotal


def opcao2(valorTotal):
    opcaoBebidas = 0
    while opcaoBebidas != 4:
        print('''========BEBIDAS=======
        [ 1 ] R$ 5,90 - Coca-cola
        [ 2 ] R$ 7,90 - Suco de laranja
        [ 3 ] R$ 4,00 - Água
        [ 4 ] Voltar\n''')

        opcaoBebidas = int(input('>>>>>>>>> Digite uma opção: '))

        if opcaoBebidas == 1:
          valorTotal += 5.90
          print('Coca-Cola adicionado com sucesso!')
          sleep(2)
          system('cls')
        elif opcaoBebidas == 2:
          valorTotal += 7.90
          print('Suuco de laranja adicionado com sucesso!')
          sleep(2)
          system('cls')
        elif opcaoBebidas == 3:
          valorTotal += 4.00
          print('Água adicionado com sucesso!')
          sleep(2)
          system('cls')
        elif opcaoBebidas == 4:
          print('Voltando ...')
          sleep(2)
          system('cls')
        else:
          print('Opção inválida! Digite novamente!')
          sleep(2)
          system('cls')
    return valorTotal
        


while n != 4:
    system('cls')   
    print( '================ MENU ==================\n'
    '      (1) Hamburguer\n'
    '      (2) Bebidas\n'
    '      (3) Valor da conta\n'
    '      (4) Fechar pedido\n')

    n = int(input('>>>> Insira o número: '))

    print('Aguarde um tempo . . .')
    sleep(3) 

    if n == 1:
        system('cls')
        valorTotal = opcao1(valorTotal)
    elif n == 2:
        system('cls')
        valorTotal = opcao2(valorTotal)
    elif n == 3:
        print('Sua conta atual está em R$ {}'.format(round(valorTotal)))
        sleep(3)
        system('cls')
    elif n == 4:
        print('Finalizando o pedido . . .')
    else:
        print('---Opção inválida. Digite novamente---')
        sleep(2)
        system('cls')
print(' Obrigado! Volte sempre!')