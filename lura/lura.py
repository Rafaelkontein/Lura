import speech_recognition as sr
import pyttsx3
import selenium
import pygame
import os

def reconhecimento():

    pyttsx3.speak('Olá, sou Lura. No que posso te ajudar?')

    microfone=sr.Recognizer() #habilita o microfone

    with sr.Microphone() as source:# usando o microfone

        print('Fale algo:')

        microfone.adjust_for_ambient_noise(source) # Isso tira os ruidos do abiente

        audio=microfone.listen(source)# Aqui estamos armazenando o

    try:
        frase = microfone.recognize_google(audio,language='pt-BR') # faz que o o algoritimo reconeça a lingua Brasileira

        print('Ok, você disse:'+ frase)

        if frase.lower() == 'toque uma música':
            pyttsx3.speak('Ok rafael,tocondo justin-biber ')
            pygame.init()
            pygame.mixer.music.load('music.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            os.system('pause')
        if frase.lower()=='abra o navegador':
            s


    except sr.UnknownValueError:
        print('desculpa não entendi...')
    return frase



reconhecimento()