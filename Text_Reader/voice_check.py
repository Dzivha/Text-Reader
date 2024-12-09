import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Index: {index} | Voice ID: {voice.id} | Name: {voice.name} | Languages: {voice.languages}")

def set_voice(index):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Set the voice by index
    engine.setProperty('voice', voices[index].id)
    return engine

# List all available voices
list_voices()

# Example of setting a voice
# Replace '0' with the index of the voice you want from the list printed above
tts_engine = set_voice(0)

# Now you can use tts_engine to speak text, and it will use the voice you selected
tts_engine.say("Hello, this is the selected voice speaking.")
tts_engine.runAndWait()
