import pyttsx3 as pt
from io import BytesIO
from pydub import AudioSegment

engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text, gender='male'):
    if gender == 'male':
        say_male(text)
    elif gender == 'female':
        say_female(text)
    else:
        print("Invalid gender option. Using male voice by default.")
        say_male(text)

def say_male(text):
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def say_female(text):
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# def save(data, filename):
#     try:
#         if isinstance(data, str):
#             engine.save_to_file(data, filename)
#             engine.runAndWait()
#         elif isinstance(data, bytes):
#             speech = AudioSegment.from_file(BytesIO(data), format="wav")
#             speech.export(filename, format="wav")
#             print(f"Audio saved to {filename} successfully!")
#         else:
#             print("Invalid data format. Expected text or audio bytes.")
#     except Exception as e:
#         print(f"Error occurred while saving audio to {filename}: {e}")