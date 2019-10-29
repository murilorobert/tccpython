import speech_recognition as spch
from time import sleep as wait
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QFileDialog

def entrada_microfone():
    reconhecedor = spch.Recognizer()
    try:
        with spch.Microphone() as micro:
            reconhecedor.adjust_for_ambient_noise(micro)
            print('\033[3;31mGravando...\033[m')
            audio = reconhecedor.listen(micro)
            print('\033[3;31mParei de Gravar\033[m')
    except spch.UnknownValueError:
        print('\033[3;31mVoz não detectada!\033[m')

    fileName, _ = QFileDialog.getSaveFileName(None,
                                            "Salvar audio", "",
                                            "Wave File (*.wav);;All Files (*)");

    print(fileName)
    #name_filewav =  input('\033[33mSalvar como:\033[0m ') + ".wav"
    if fileName:
        with open(fileName, 'wb') as file:
            file.write(audio.get_wav_data())
            wait(1)
            print('\033[3;32mSalvo com sucesso!')
            transc_file(fileName)


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
            return 'Não consegui entender a voz do arquivo!'

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
