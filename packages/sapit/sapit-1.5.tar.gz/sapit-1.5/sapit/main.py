import pyttsx3 as pt
from io import BytesIO
from pydub import AudioSegment

engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(script, gender='male', volume=1.0, pitch=1.0):
    if gender == 'male':
        say_male(script, volume, pitch)
    elif gender == 'female':
        say_female(script, volume, pitch)
    else:
        print("Invalid gender option. Using male voice by default.")
        say_male(script)

def say_male(script, volume=1.0, pitch=1.0):
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', volume)
    engine.setProperty('pitch', pitch)
    engine.say(script)
    engine.runAndWait()

def say_female(script, volume=1.0, pitch=1.0):
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', volume)
    engine.setProperty('pitch', pitch)
    engine.say(script)
    engine.runAndWait()

def save(script, filename, volume=1.0, pitch=1.0):
    try:
        if isinstance(script, str):
            engine.setProperty('volume', volume)
            engine.setProperty('pitch', pitch)
            engine.save_to_file(script, filename)
            engine.runAndWait()
        elif isinstance(script, bytes):
            speech = AudioSegment.from_file(BytesIO(script), format="wav")
            adjusted_speech = speech + volume
            adjusted_speech = speech.speedup(playback_speed=pitch)
            adjusted_speech.export(filename, format="wav")
            print(f"Audio saved to {filename} successfully!")
        else:
            print("Invalid data format. Expected text or audio bytes.")
    except Exception as e:
        print(f"Error occurred while saving audio to {filename}: {e}")
