import speech_recognition as sr


# Função responsável para reconhecer a fala
def ouvir_microfone():
# Habilita o microfone para ouvir o usuario

microfone = sr.Recognizer()
    with sr.Microphone() as source:
    #Chama a função de redução de rúido disponível na lib
    microfone.adjust_for_ambient_noise(source)
    #Avisa o usuário que está pronto para ouvir
    print('Diga alguma coisa: ')
    audio = microfone.listen(source)