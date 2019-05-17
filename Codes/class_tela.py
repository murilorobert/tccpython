from os import system as sistema
import capta_audio

def limpa_tela():
    sistema('cls' if sistema == 'nt' else 'clear')

def menu_inicial():
    print('\033[34m{:=^48}'.format('\033[34m Áspide Recognizer V1.0 \033[34m'))
    print('''\033[0mFunções da ferramenta:
    [ 0 ] - Entrada por microfone
    [ 1 ] - Entrada por arquivo ''')
    print('\033[34m=\033[0m' * 39)

def funcoes_ferramenta():
    repetir = 's'
    while repetir == 's' or repetir == 'S':
        menu_inicial()
        opcao = str(input('\033[33mFunção >>>\033[0m '))
        if opcao == '0':
            capta_audio.entrada_microfone()
            repetir = str(input('\033[33mQuer usar o software novamente? [s/n]\033[0m '))
            limpa_tela()
        elif opcao == '1':
            capta_audio.entrada_file()
            repetir = str(input('\033[33mQuer usar o software novamente? [s/n]\033[0m '))
            limpa_tela()
        else:
            print('\033[3;31mOpção inválida!\033[0m')
            repetir = str(input('\033[33mQuer tentar novamente? [s/n]\033[0m '))
