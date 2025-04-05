import speech_recognition as sr
import pyautogui
import time
import pyttsx3
import threading

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech from the microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand the command.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

# Global variables to control mouse movement and scrolling
moving_right = False
moving_left = False
moving_up = False
moving_down = False
moving_top_right = False
moving_top_left = False
moving_bottom_right = False
moving_bottom_left = False
stop_moving = False
scroll_up = False
scroll_down = False
stop_scrolling = False

# Function to perform actions based on recognized commands
def perform_action(command):
    global moving_right, moving_left, moving_up, moving_down
    global moving_top_right, moving_top_left, moving_bottom_right, moving_bottom_left
    global stop_moving, scroll_up, scroll_down, stop_scrolling

    print(f"Received command: {command}")  # Debug print to show the command in the console

    if 'move mouse up' in command or 'move up' in command:
        stop_moving = False
        moving_up = True
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse up")
    elif 'move mouse down' in command or 'move down' in command:
        stop_moving = False
        moving_down = True
        moving_up = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse down")
    elif 'move mouse left' in command or 'move left' in command:
        stop_moving = False
        moving_left = True
        moving_up = False
        moving_down = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse left")
    elif 'move mouse right' in command or 'move right' in command:
        stop_moving = False
        moving_right = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse right")
    elif 'move top right' in command:
        stop_moving = False
        moving_top_right = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse top right")
    elif 'move top left' in command:
        stop_moving = False
        moving_top_left = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Moving mouse top left")
    elif 'move bottom right' in command:
        stop_moving = False
        moving_bottom_right = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_left = False
        speak("Moving mouse bottom right")
    elif 'move bottom left' in command:
        stop_moving = False
        moving_bottom_left = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        speak("Moving mouse bottom left")
    elif 'stop moving' in command:
        stop_moving = True
        moving_up = False
        moving_down = False
        moving_left = False
        moving_right = False
        moving_top_right = False
        moving_top_left = False
        moving_bottom_right = False
        moving_bottom_left = False
        speak("Stopping mouse movement")
    elif 'left click' in command:  # Left click
        pyautogui.click()  # Perform left click
        speak("Left clicking")
    elif 'right click' in command:  # Right click
        pyautogui.click(button='right')  # Perform right click
        speak("Right clicking")
    elif 'double click' in command:
        pyautogui.doubleClick()  # Perform double click
        speak("Double clicking")
    elif 'scroll up' in command:
        scroll_up = True
        scroll_down = False
        stop_scrolling = False
        speak("Scrolling up continuously")
    elif 'scroll down' in command:
        scroll_down = True
        scroll_up = False
        stop_scrolling = False
        speak("Scrolling down continuously")
    elif 'stop scrolling' in command:
        stop_scrolling = True
        scroll_up = False
        scroll_down = False
        speak("Stopping scrolling")
    elif 'exit' in command:
        speak("Exiting program")
        return False  # Exit the loop
    else:
        speak(f"Sorry, I didn't recognize the command: {command}")  # Speak the unrecognized command

    return True

# Function to perform continuous movement of the mouse
def move_mouse():
    global moving_right, moving_left, moving_up, moving_down
    global moving_top_right, moving_top_left, moving_bottom_right, moving_bottom_left
    while True:
        if stop_moving:
            time.sleep(0.1)  # Delay to avoid high CPU usage when idle
            continue

        if moving_up:
            pyautogui.move(0, -1)  # Move mouse up slowly (1 pixel per iteration)
        elif moving_down:
            pyautogui.move(0, 1)  # Move mouse down slowly (1 pixel per iteration)
        elif moving_left:
            pyautogui.move(-1, 0)  # Move mouse left slowly (1 pixel per iteration)
        elif moving_right:
            pyautogui.move(1, 0)  # Move mouse right slowly (1 pixel per iteration)
        elif moving_top_right:
            pyautogui.move(1, -1)  # Move mouse top-right diagonally
        elif moving_top_left:
            pyautogui.move(-1, -1)  # Move mouse top-left diagonally
        elif moving_bottom_right:
            pyautogui.move(1, 1)  # Move mouse bottom-right diagonally
        elif moving_bottom_left:
            pyautogui.move(-1, 1)  # Move mouse bottom-left diagonally

        time.sleep(0.05)  # Adjust this for desired movement speed

# Function to continuously scroll up or down
def scroll_screen():
    global scroll_up, scroll_down, stop_scrolling
    while True:
        if stop_scrolling:
            time.sleep(0.1)  # Delay to avoid high CPU usage when idle
            continue

        if scroll_up:
            pyautogui.scroll(50)  # Scroll up continuously (50 pixels)
        elif scroll_down:
            pyautogui.scroll(-50)  # Scroll down continuously (-50 pixels)

        time.sleep(0.1)  # Adjust this for desired scrolling speed

# Main function to start the voice-controlled system
def main():
    # Start the mouse movement and scrolling in separate threads
    threading.Thread(target=move_mouse, daemon=True).start()
    threading.Thread(target=scroll_screen, daemon=True).start()

    while True:
        command = listen()
        if command:
            if not perform_action(command):
                break

if __name__ == "__main__":
    main()
