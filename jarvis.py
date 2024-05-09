import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        print("Wait for Few Moments...")
        query=r.recognize_google(audio,language='eg-in')
        print(f"You just said:{query}\n")
    except Exception as e:
        print(e)
        speak("Sorry I didn't get that. Please say again.")  
        query="none"
    return query

def wishings():
    hour=int(datetime.datetime.now().hour)
    if 4<=hour<12:
        speak("Good Morning Boss!")
    elif 12<=hour<16:
        speak("Good Afternoon Boss!")
    elif 16<=hour<23:
        speak("Good Evening Boss!")
    else:
        speak("Good Night Boss!")

def open_social_media(platform):
    social_media_urls = {
        "facebook": "https://www.facebook.com/",
        "twitter": "https://twitter.com/",
        "instagram": "https://www.instagram.com/",
        "linkedin": "https://www.linkedin.com/"
        # Add more social media platforms and their URLs as needed
    }

    if platform in social_media_urls:
        url = social_media_urls[platform.lower()]
        webbrowser.open(url)
        print(f"Opening {platform}...")
    else:
        print("Sorry, this social media platform is not supported.")


if __name__=="__main__":
    wishings()
    social_media =input("Which social media platform do you want to open? (e.g., Facebook, Twitter, Instagram, LinkedIn): ")
    query=commands().lower()
    open_social_media(social_media)
    if 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M")
        print(strTime)
        speak(f"sir,time is {strTime}")
    elif 'chrome' in query:
        speak("Opening Google chorme sir...")
        os.startfile("C:\\Program Files\Google\Chrome\Application\chrome.exe")
    
    elif 'wikipedia' in query:
        speak('Searching in Wikipedia...')
        try:
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        except:
            speak("Sorry, I couldn't find what you were looking for.")
            print("No result found..")
