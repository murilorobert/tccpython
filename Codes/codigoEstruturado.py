import os
import speech_recognition as spch
from gtts import gTTS
import playsound
from time import sleep as wait
#print(spch.Microphone.list_microphone_names())

os.system('cls' if os.name == 'nt' else 'clear') 
resp = 's'
#Função responsável por criar o arquivo de áudio e executá-lo
def cria_audio (audio):
    tts = gTTS(audio, lang='pt-br')
    #Salva o file de audio
    tts.save('/home/robertdccaetano/Música/local/captura.mp3')
    #Executa o file de audio
    playsound.playsound('/home/robertdccaetano/Música/local/captura.mp3')

while(resp == 's'):
    r = spch.Recognizer()
    with spch.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print('\033[35mOlá! Eu sou seu computador, vamos lá diga alguma coisa para nós conversarmos... \033[m')
        audio = r.listen(mic)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print('\033[33mCalma aí vou anotar o que você me falou, primeiro me informe onde quer salvar seu arquivo... \033[m')
            wait(2)
            try:
                nome_arquivo = input('\033[3;31mDigite caminho/nomearquivo.txt para salvá-lo:     ')
                arquivo = open(nome_arquivo,  'w')
                arquivo.write(text)
                print('\033[4;32mEu te entendi, legal! Parece que você quis me dizer, {}?\033[m'.format(text))       
                arquivo.close()
                cria_audio(text)                
                resp = 'n'
            except FileNotFoundError:
                print('Caminho incorreto')
                nome_arquivo = input('Tente novamente: ')
        except spch.UnknownValueError:
            print('\033[31mNão te entendi me desculpe... :/ ')
            resp = input('Quer tentar novamente? [S/N]] ')
            os.system('cls' if os.name == 'nt' else 'clear')            
