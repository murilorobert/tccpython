from os import system as sistema
import capta_audio

def limpa_tela():
    sistema('cls' if sistema == 'nt' else 'clear')

def menu_inicial():
    print('{:=^40}'.format(' Áspide Recognizer V1.0 '))

def opcoes_ferramenta():
    print('''Funções da ferramenta:
    [ 0 ] - Entrada por microfone
    [ 1 ] - Entrada por arquivo ''')
    opcao = int(input('Opção: '))
    if opcao == 0:
        capta_audio.entrada_microfone()
    elif opcao == 1:
        print('Opção por arquivo')
    else:
        print('Opção invalida')


