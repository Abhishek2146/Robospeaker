import win32com.client as wincom

if __name__ == '__main__' :
    print("Welcome to Robospeaker. Created by Abhishek!")
    speak = wincom.Dispatch("SAPI.Spvoice")
    while True:

        x = input("Enter what you want me to speak:")
        if x == "q":
            speak.speak("bye bye friend")
            break
        command = f"{x}"
        speak.speak(command)