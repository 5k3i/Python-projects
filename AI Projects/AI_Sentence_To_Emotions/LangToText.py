import speech_recognition as sr
import pyaudio


def pull_mic_audio(speak_time) :
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=speak_time)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)
        return text


def main() :
    print(pull_mic_audio(2))

if __name__ == '__main__':
    main()