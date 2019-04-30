import os
import speech_recognition as sr
from time import sleep as wait

os.system('cls' if os.name == 'nt' else 'clear') 
#print(sr.Microphone.list_microphone_names())
resp = 's'
while(resp == 's'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('\033[35mOlá! Eu sou seu computador, vamos lá diga alguma coisa para nós conversarmos... \033[m')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print('\033[33mCalma aí vou anotar o que você me falou, primeiro me informe onde quer salvar seu arquivo... \033[m')
            wait(3)
            try:
                nome_arquivo = input('\033[3;31mDigite o caminho+nome para salvar seu arquivo Ex: /path/nomearquivo.txt:  ')
                arquivo = open(nome_arquivo,  'w')
                arquivo.write(text)
                print('\033[4;32mEu te entendi, legal! Parece que você quis me dizer, {}?\033[m'.format(text))       
                arquivo.close()
            except FileNotFoundError:
                print('Caminho incorreto')
        except sr.UnknownValueError:
            print('\033[31mNão te entendi me desculpe... :/ ')
            resp = input('Quer tentar novamente ? [S/N]] ')
            os.system('cls' if os.name == 'nt' else 'clear')            
