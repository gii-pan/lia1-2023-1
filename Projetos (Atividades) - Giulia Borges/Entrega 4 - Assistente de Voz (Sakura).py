# Assistente online Sakura!

# import speech_recognition as sr
#
# # Criar um reconhecedor de voz
# r = sr.Recognizer()
#
# # Abrir o microfone para capturar áudio
# with sr.Microphone() as source:
#     while True:
#         # Definir microfone como fonte de áudio
#         audio = r.listen(source)
#
#         try:
#             print(r.recognize_google(audio, language='pt'))
#         except sr.UnknownValueError:
#             pass


# Assistente offline Sakura!

from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model(model_name='vosk-model-small-pt-0.3')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
