from os import system as sistema

def limpa_tela():
    sistema('cls' if sistema == 'nt' else 'clear')

def menu_inicial():
    print('{:=^40}'.format(' Áspide Recognizer V1.0 '))
