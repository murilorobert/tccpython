import speech_recognition as spch
from time import sleep as wait

def entrada_microfone():
    reconhecedor = spch.Recognizer()
    try:
        with spch.Microphone() as micro:
            reconhecedor.adjust_for_ambient_noise(micro)
            print('\033[3;31mGravando...\033[m')
            audio = reconhecedor.listen(micro)
    except spch.UnknownValueError:
        print('\033[3;31mVoz não detectada!\033[m')

    name_filewav =  input('\033[33mSalvar como:\033[0m ') + ".wav"
    with open(name_filewav, 'wb') as file:
        file.write(audio.get_wav_data())
        wait(1)
        print('\033[3;32mSalvo com sucesso!')
        transc_file(name_filewav)


def transc_file(path):
    reconhecedor = spch.Recognizer()
    with spch.AudioFile(path) as source:
        try:
            arquivo = reconhecedor.record(source)
            transcrito = reconhecedor.recognize_google(arquivo, language="pt-br")
            print('\033[3;32mTranscrevendo...\033[0m')
            wait(1)
            print('\033[1mResultado >>> ({})\033[0m'.format(transcrito))
            #print(reconhecedo.recognize_google(arquivo, language="pt-br"))
            return transcrito
        except spch.UnknownValueError:
            print('\033[3;31mNão consegui entender a voz do arquivo!\033[m')


def entrada_file():
    repetir = 's'
    while repetir == 's' or repetir == 'S':
        try:
            caminho_file = str(input('\033[33mDigite o caminho ou nome do arquivo:\033[0m ') + '.wav')
            transc_file(caminho_file)
            repetir = 'n'
        except FileNotFoundError:
            print('\033[3;31mArquivo ou caminho incorreto!\033[0m')
            repetir = str(input('\033[0;33mQuer tentar novamente? [s/n] '))
