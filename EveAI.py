import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import openai

openai.api_key = 'your-key-here'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


pre_written_responses = {
    'bye': {'response': 'Goodbye!', 'action': lambda: exit()},
    'see you': {'response': 'Goodbye!', 'action': lambda: exit()},
    'goodbye': {'response': 'Goodbye!', 'action': lambda: exit()},
    'thank': {'response': 'No reason to thank me, it\'s my job as your personal assistant.', 'action': None},
    'who are you': {'response': 'I am your personal virtual assistant, Eve', 'action': None},
    'what is the weather like': {'response': 'Opening weather information...', 'action': lambda: webbrowser.open("https://www.google.com/search?client=opera-gx&q=weather&sourceid=opera&ie=UTF-8&oe=UTF-8")},
    'open youtube': {'response': 'Opening YouTube...', 'action': lambda: webbrowser.open("https://www.youtube.com/")},
    'open google': {'response': 'Opening Google...', 'action': lambda: webbrowser.open("https://www.google.com/")},
    'what is the time': {'response': '', 'action': lambda: speak(f"At the moment, the time is {datetime.datetime.now().strftime('%H:%M')}")},
    'stop': {'response': 'Stopping.', 'action': lambda: exit()},
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Your AI Assistant Eve is here.")

def takeCommand():
    global choice
    if 'choice' not in globals():
        speak("Do you want to type or speak?")
        print("Do you want to type or speak?")
        choice = input("Type 't' for text or 's' for speech. Type 'e' to exit: ").lower()
        if choice == 'e':
            exit()
        while choice not in ['t', 's']:
            speak("Invalid choice. Please type 't' for text or 's' for speech.")
            choice = input("Type 't' for text or 's' for speech. Type 'e' to exit: ").lower()
    if choice == 's':
        return takeCommandSpeech()
    elif choice == 't':
        return input("Type your command: ").lower()

def takeCommandSpeech():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except:
            speak('Sorry, I couldn\'t catch that. Can you say it again?')
            continue

def chatGPT(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt}\n",
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

def execute_action(query):
    for key, pre_written_response in pre_written_responses.items():
        if key in query and key not in ['bye', 'see you', 'goodbye', 'stop']:
            if pre_written_response['action']:
                pre_written_response['action']()
            speak(pre_written_response['response'])
            return True

    for key in ['bye', 'see you', 'goodbye', 'stop']:
        if key in query:
            if pre_written_responses[key]['action']:
                speak(pre_written_responses[key]['response'])
                pre_written_responses[key]['action']()
            return True
    return False

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'change' in query and ('text' in query or 'speak' in query):
            choice = 't' if 'text' in query else 's'
            speak(f"Switching to {'text' if choice == 't' else 'speech'} mode.")
            continue

        if not execute_action(query):
            gpt_prompt = f"The user said: {query}\nEve's response:"
            response = chatGPT(gpt_prompt)
            if response:
                print(response)
                speak(response)