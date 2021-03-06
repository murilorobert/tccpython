import os
import speech_recognition as spch
import pygame
from gtts import gTTS
from time import sleep as wait
#print(spch.Microphone.list_microphone_names())
os.system('cls' if os.name == 'nt' else 'clear')
resp = 's'

#Função responsável por criar o arquivo de áudio e executá-lo
def cria_audio (som):
    tts = gTTS(som, lang='pt-br')
    #Salva o file de audio
    nome_audio = input('\033[33mDigite nome do arquivo de audio: ') + ".mp3"
    tts.save(nome_audio)
    #Executa o file de audio através do modulo pyGame
    pygame.mixer.init()
    pygame.mixer.music.load(nome_audio)
    pygame.mixer.music.play()
    encerrar = input('\033[32mPressione ENTER para finalizar... ')

while(resp == 's'):
    r = spch.Recognizer()
    with spch.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print('\033[32mOlá, sou seu computador me diga alguma coisa para nós conversarmos... \033[m')
        audio = r.listen(mic)
    with open("microphone-result.wav", "wb") as f:
        f.write(audio.get_wav_data())
        try:
            text = r.recognize_sphinx(audio)
            print('\033[32mCalma aí vou anotar o que você me falou, primeiro me informe onde quer salvar seu arquivo. \033[m')
            wait(1)
            try:
                nome_arquivo = input('\033[33mDigite o (nomeDoArquivo.txt) para salvá-lo: ')
                arquivo = open(nome_arquivo,  'w')
                arquivo.write(text)
                print('\033[1;32mParece que você quis me dizer, {}?\033[m'.format(text))
                arquivo.close()
                resp = 'n'
            except FileNotFoundError:
                print('\033[1;31mCaminho incorreto')
                nome_arquivo = input('\033[31mTente novamente: ')
        except spch.UnknownValueError:
            print('\033[31mNão te entendi me desculpe... :/ ')
            resp = input('\033[1;31mQuer tentar novamente? [S/N]]' '\033[m')
            os.system('cls' if os.name == 'nt' else 'clear')
