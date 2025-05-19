import speech_recognition as sr
import pyaudio
from emotionclassifier import EmotionClassifier

classifier = EmotionClassifier()

response_dict = {
    "joy": "I'm glad to hear that you're feeling happy!",
    "anger": "I understand that you're feeling angry. It's okay to feel that way sometimes.",
    "fear": "I can sense that you're feeling scared. It's important to talk about your fears.",
    "sadness": "I'm sorry to hear that you're feeling sad. It's okay to feel that way sometimes.",
    "disgust": "I can sense that you're feeling disgusted. It's important to talk about your feelings.",
    "surprise": "I can sense that you're feeling surprised. It's important to talk about your feelings.",
    "neutral": "I can sense that you're feeling neutral. It's important to talk about your feelings."
}

def pull_mic_audio():
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
        init_rec.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio_data = init_rec.listen(source, timeout=5)
            print("Recognizing your text.............")
            text = init_rec.recognize_google(audio_data)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
            return None
    return text

def pull_emotion(input_text, classifier) :
    result = classifier.predict(input_text)
    return result

def main() :
    user_speech = pull_mic_audio()

    emotion_analysis = pull_emotion(user_speech, classifier)['label']

    print(response_dict[emotion_analysis])

if __name__ == '__main__':
    main()
