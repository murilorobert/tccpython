import speech_recognition as sr

sr.Microphone.list_microphone_names()

'''r = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga algo: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Voce disse: {}'.format(text))
    except sr.UnknownValueError:
        print('Não te entendi me desculpe.')
'''
