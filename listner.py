import os
import gradio as gr
import random
from pydub import AudioSegment
import speech_recognition as sr
#copy righted to : Ahmed hemida
# Function to convert audio to WAV and recognize speech
def transcribe_audio(audio_file, language):
    # Get the file extension
    file_extension = os.path.splitext(audio_file.name)[1].lower()

    if file_extension not in (".mp3", ".ogg"):
        return "Unsupported file format. Please upload an MP3 or OGG file."

    if file_extension == ".mp3":
        # Convert the uploaded MP3 file to WAV format
        sound = AudioSegment.from_mp3(audio_file.name)
    elif file_extension == ".ogg":
        # Convert the uploaded OGG file to WAV format
        sound = AudioSegment.from_ogg(audio_file.name)

    wav_file = "output.wav"
    sound.export(wav_file, format="wav")

    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the WAV file as the audio source
    with sr.AudioFile(wav_file) as source:
        # Read the entire audio file
        audio_data = r.record(source)
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio_data, language=language)
    
    # Generate a random integer
    RAZNY = random.randint(0, 9)

    return f"{text}"

# Create a Gradio interface
input_components = [
    gr.inputs.File(label="Upload an MP3 or OGG File"),
    gr.inputs.Dropdown(label="Language", choices=["en-US", "ar-EG"], default="en-US"),
]

output_component = gr.outputs.Textbox(label="Transcription Result")

gr.Interface(transcribe_audio, inputs=input_components, outputs=output_component, capture_session=True).launch(share=True)
