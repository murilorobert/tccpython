import speech_recognition as sr
from time import sleep as wait

print(sr.Microphone.list_microphone_names())


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('\033[35mOlá! Eu sou seu computador, vamos lá diga alguma coisa para nós conversarmos... \033[m')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        print('\033[2;30mCalma aí vou anotar o que você me falou, preciso aprender mais sobre humanos rs =D \033[m')
        wait(5)
        print('\033[4;32mEu te entendi, legal! Parece que você quis me dizer, {}?\033[m'.format(text))
    except sr.UnknownValueError:
        print('\033[31mNão te entendi me desculpe, execute-me novamente!')
