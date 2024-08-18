from dotenv import load_dotenv 
import os
import pyaudio
import wave
import openai
from google.cloud import speech


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/nahia/Downloads/voice-ai-432806-c232ffa6b92c.json"



def record_audio(filename, duration=5):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    p = pyaudio.PyAudio()

    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    print("Recording...")
    frames = []
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    print("Recording finished")
    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def transcribe_audio(filename):
    client = speech.SpeechClient()
    with open(filename, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
        return result.alternatives[0].transcript   

conversation_history = []
def get_openai_response(text):
    conversation_history.append(f"User: {text}")
    prompt = "\n".join(conversation_history) + "\nAI:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    ai_response = response.choices[0].message['content'].strip()
    conversation_history.append(f"AI: {ai_response}")
    return ai_response


    


# if __name__ == "__main__":
#     filename = "output.wav"
    
#     record_audio(filename)
#     text = transcribe_audio(filename)
#     print(f"Recognized Text: {text}")




        


    



