'''
gTTS --> Google text to Speech
playsound --> pip install playsound==1.2.2
pyaudio --> pip install pyaudio

3 Functions -->1)Listen (SpeechRecognition)
               2)respond (gtts)
               3)Assistant (Conditions) -->Conversation,Greeting,datetime,locate a place,open a browser,play a youtube video

from gtts import gTTS
import playsound
text = gTTS("Hello guys,how are you doing?")
text.save("audio.mp3")
playsound.playsound("audio.mp3")

'''
#Import the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import qrcode
import re

#let us create listen function
def listen():
    """Function for Speech Recogntion"""
    r = sr.Recognizer()
    #we will take microphone as source
    try:
        with sr.Microphone() as source:
            print("Ika modaledadamma")
            audio = r.listen(source, phrase_time_limit=10)
    except Exception as e:
        print("Microphone error or not available:", e)
        return ""
    #we need to give our text as voice
    data = ""
    #here we will give exceptions (try,except)
    try:
        data = r.recognize_google(audio)
        print("You said:", data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speak clearly request is failing")
    return data


def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    #we are using uuid --> to randomize the content in the
    #audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def create_qr_flow():
    """Prompts user for QR code details and generates the QR code image."""
    respond("What text or link would you like to put in the QR code?")
    qr_data = listen()

    # Fallback to console input if speech recognition did not capture anything
    if not qr_data or not qr_data.strip():
        respond("I could not hear that. Please type the text or link in the terminal.")
        try:
            qr_data = input("Enter QR code text or URL: ").strip()
        except EOFError:
            qr_data = ""

    if not qr_data:
        respond("No details provided. Cancelling QR code creation.")
        return

    respond("What should I name the QR code file?")
    file_name = listen()

    if not file_name or not file_name.strip():
        # Fallback to a default timestamped name if user did not provide one
        file_name = f"qrcode_{int(time.time())}"
    else:
        # Sanitize the filename for Windows
        file_name = re.sub(r'[\\/*?:"<>|]', "", file_name).strip()
        file_name = file_name.replace(" ", "_")
        if not file_name:
            file_name = f"qrcode_{int(time.time())}"

    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)

        abs_path = os.path.abspath(file_name)
        respond(f"Your QR code has been created and saved as {file_name}")
        print(f"QR code successfully saved at: {abs_path}")

        # Open the image preview
        try:
            os.startfile(abs_path)
        except Exception:
            pass
    except Exception as e:
        print(f"Error creating QR code: {e}")
        respond("Sorry, there was an error creating the QR code.")


#here we will make our virtual assitant into action

def va(data):
    """Our Virtual Assistant with the actions"""
    listening = True
    data_lower = data.lower() if data else ""
    if "how are you" in data_lower:
        respond("I am fine thanks for asking")
    elif "what are your plans" in data_lower:
        respond("Only Study..One focus in 2026")
    elif "how are things going" in data_lower:
        respond("Anthaa okay ika nenu settle avvali")
    elif "time" in data_lower:
        respond(time.ctime())
    elif "qr" in data_lower:
        create_qr_flow()
    elif "stop talking" in data_lower or "bye" in data_lower:
        listening = False
        respond("okay cool.. kopadakuu bye")
    elif data_lower:
        print("Command not recognized, please try again.")
    else:
        print("Make sure to speak louder and faster")

    return listening


if __name__ == "__main__":
    respond("Hey Harsha.. Good to hear from you. How are you?")
    listening = True
    while listening:
        data = listen()
        listening = va(data)
