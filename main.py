import speech_recognition as sr
import os
import pyttsx3  

def initialize_speaker():
    """Initialize the speaker for text-to-speech."""
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)  # Set the speech speed
    return speaker

def voice_input(speaker):
    """Capture and return voice input as text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")  
        speaker.say("Listening...")
        speaker.runAndWait()  

        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower().strip()  # Convert speech to text
            print(f"DEBUG: Recognized Command -> {command}")  # Debug output
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speaker.say("Sorry, I did not understand that.")  
            speaker.runAndWait()  
            return None
        except sr.RequestError:
            print("Speech recognition service error.")
            speaker.say("Speech recognition service error.")
            speaker.runAndWait()
            return None

def main():
    speaker = initialize_speaker()  

    message = """Welcome! Let's choose the mode for controlling the mouse.
                Please select what you want me to enable from below:
                  1. Voice based mouse control
                  2. Hand based mouse control
                  3. Exit
                  Say the option you want to enable."""
    print(message)
    speaker.say(message)  
    speaker.runAndWait()  

    while True:
        command = voice_input(speaker)  
        
        if command:
            # Normalize and check for variations of "one", "two", "three"
            if any(word in command for word in ["voice based mouse control", "one", "1", "won"]):
                speaker.say("Executing voice-based mouse control...")  
                speaker.runAndWait()  
                print("Executing voice-based mouse control...")
                os.system('python Voice_control.py')  
                break  
            elif any(word in command for word in ["hand based mouse control", "two", "2", "to"]):
                speaker.say("Executing hand-based mouse control...")  
                speaker.runAndWait()  
                print("Executing hand-based mouse control...")
                os.system('python Hand_gesture.py')  
                break  
            elif any(word in command for word in ["exit", "three", "3", "free"]):
                print("Exiting the program...")
                speaker.say("Exiting the program...")  
                speaker.runAndWait()  
                break  
            else:
                print(f"Sorry, I did not understand that: {command}.")
                speaker.say(f"Sorry, I did not understand that.")  
                speaker.runAndWait()  
        else:
            print("Please try again.")
            speaker.say("Please try again.")  
            speaker.runAndWait()  

if __name__ == "__main__":
    main()
