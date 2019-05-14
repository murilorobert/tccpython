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

    name_filewav =  input('\033[33mSalvar como: ') + ".wav"
    with open(name_filewav, 'wb') as file:
        file.write(audio.get_wav_data())
        wait(1)
        print('\033[3;32mSalvo com sucesso!')
        trans_file(name_filewav)


def trans_file(path):
    r = spch.Recognizer()
    with spch.AudioFile(path) as source:
        try:
            arquivo = r.record(source)
            transcrito = r.recognize_sphinx(arquivo)
            print('\033[3;32mTranscrevendo...\033[m')
            wait(1)
            print('\033[1m({})'.format(transcrito))
            #print(reconhecedor.recognize_google(arquivo, language="pt-br"))
        except spch.UnknownValueError:
            print('\033[3;31mNão consegui entender a voz do arquivo!\033[m')
