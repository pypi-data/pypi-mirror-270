import pyttsx3 as pt
from io import BytesIO
from pydub import AudioSegment

# Initialize pyttsx3 engine
engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text):
    try:
        # Convert text to speech
        engine.say (text)
        engine.runAndWait()
        return 'temp.wav'
    except Exception as e:
        print(f"Error occurred while saying {text}: {e}")

# def save(data, filename):
#     try:
#         if isinstance(data, str):
#             # If data is text, save it directly to an audio file
#             engine.save_to_file(data, filename)
#             engine.runAndWait()
#         elif isinstance(data, bytes):
#             # If data is audio bytes, save it to the specified filename
#             speech = AudioSegment.from_file(BytesIO(data), format="wav")
#             speech.export(filename, format="wav")
#             print(f"Audio saved to {filename} successfully!")
#         else:
#             print("Invalid data format. Expected text or audio bytes.")
#     except Exception as e:
#         print(f"Error occurred while saving audio to {filename}: {e}")

# Example usage:
# s = say("Hello")
# save(s, 'p.wav')
