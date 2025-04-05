# 🎯 Voice and Hand Gesture Controlled Virtual Mouse

This project allows users to control their computer mouse using **voice commands** or **hand gestures**, enabling accessible interaction for people with physical disabilities.

---

## ✅ Prerequisites

- Windows, macOS, or Linux
- Webcam and Microphone
- Visual Studio Code (VS Code) Installed

---

## 🐍 Step 1: Install Python 3.8.5

> ⚠️ The project requires **Python 3.8.5** specifically for compatibility with some packages.

### 👉 Install Python 3.8.5:

1. Go to the [official Python releases page](https://www.python.org/downloads/release/python-385/)
2. Download the installer for your OS:
   - Windows: `python-3.8.5-amd64.exe`
   - macOS/Linux: Choose the corresponding version
3. **During installation:**
   - ✅ Check “Add Python to PATH”
   - ⚙️ Choose “Customize Installation” if needed
   - Complete the installation

---

## 🛠️ Step 2: Set Python 3.8.5 in VS Code 

1. Open **VS Code**
2. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac)
3. Type: `Python: Select Interpreter`
4. Choose the Python 3.8.5 interpreter (should look like: `Python 3.8.5 64-bit`)
   - If not visible, click **Enter interpreter path** and locate:  
     `C:\Users\<yourname>\AppData\Local\Programs\Python\Python38\python.exe`

---

## 📦 Step 3: Install Dependencies

> Install all required libraries in your **Python 3.8.5 environment** using pip.

Create a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate # On Windows
source venv/bin/activate # On macOS/Linux
Then install the required libraries:

```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio

---

### ❗ If `pyaudio` Installation Fails (on Windows):
pip install pipwin
pipwin install pyaudio


# PROJECT STRUCTURE
├── main.py             # Main entry file – lets you choose control mode by voice
├── Voice_control.py    # Handles voice-based mouse actions
├── Hand_gesture.py     # Handles hand gesture recognition and mouse control
```
---
## 🚀 Step 4: Run the Program
```bash
python main.py
```
You'll be prompted to choose your input mode (voice or hand gesture).
Just say "voice based mouse control", "hand based mouse control", or "exit" to proceed.


📌 Requirements Summary
Python 3.8.5
opencv-python
mediapipe
pyautogui
speechrecognition
pyttsx3
pyaudio

