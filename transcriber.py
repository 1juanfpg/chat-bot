import openai

#Convertir audio en texto
class Transcriber:
    def __init__(self):
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def transcribe(self, audio):
        try:
            audio.save("audio.mp3") 
            audio_file= open("audio.mp3", "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            print(transcript)
            return transcript.text
        except Exception as e:
            # Manejo de otras excepciones
            print("Ocurrió una excepción:", e)