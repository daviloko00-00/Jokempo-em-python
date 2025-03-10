from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

def jokempo():
    print('Jokempo!!! Escolha sua opção:')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    print('0 - Sair')
    opcao = int(input('Digite sua opção: '))
    if opcao == 0:
        print('Saindo...')
        return
    elif opcao < 1 or opcao > 3:
        print('Opção inválida')
        return

    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po!!!')
    sleep(1)

    computador = randint(1, 3)

    print('-=' * 11)
    print(f'Computador jogou {itens[computador - 1]}')
    print(f'Jogador jogou {itens[opcao - 1]}')
    print('-=' * 11)

    if computador == 1:
        if opcao == 1:
            print('Empate')
        elif opcao == 2:
            print('Você ganhou')
        elif opcao == 3:
            print('Você perdeu')
    
    elif computador == 2:
        if opcao == 2:
            print('Empate')
        elif opcao == 3:
            print('Você ganhou')
        elif opcao == 1:
            print('Você perdeu')

    elif computador == 3:
        if opcao == 3:
            print('Empate')
        elif opcao == 1:
            print('Você ganhou')
        elif opcao == 2:
            print('Você perdeu')

jokenpo()
