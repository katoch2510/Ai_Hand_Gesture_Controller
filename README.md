🤖 AI Hand Gesture Control System

An AI-powered hand gesture control system that allows users to control mouse actions, media playback, system volume, browser navigation, and YouTube controls using real-time hand gestures via a webcam.
Built using Python, OpenCV, and MediaPipe, this project demonstrates practical use of Computer Vision + Human–Computer Interaction (HCI).

🚀 Features

🖱️ Mouse control (move, left click, right click, drag & drop)

🔊 Smart volume control

System volume

YouTube volume (context-aware)

⏯️ Media controls (play / pause, next, previous)

🌐 Open Browser & YouTube using gestures

🧠 AI confidence filtering to reduce false gestures

📂 File navigation using swipe gestures

🎥 Real-time hand tracking using webcam

🧠 How It Works

Hand Detection – MediaPipe detects hand landmarks in real time

Gesture Recognition – Finger positions are analyzed to identify gestures

Context Awareness – Active window (YouTube / Browser / Files) is detected

Action Execution – Mouse, media, or system actions are triggered using PyAutoGUI

🛠️ Tech Stack

Python

OpenCV

MediaPipe

PyAutoGUI

PyGetWindow

Computer Vision

Human–Computer Interaction (HCI)

📁 Project Structure
AI-Hand-Gesture-Control/
│
├── main.py                 # Main execution file
├── hand_tracking.py        # Hand detection using MediaPipe
├── gesture_recognition.py  # Gesture logic & mapping
├── mouse_control.py        # Mouse actions
├── media_control.py        # Media & volume control
├── file_control.py         # File navigation
├── app_control.py          # Open browser / YouTube
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/AI-Hand-Gesture-Control.git
cd AI-Hand-Gesture-Control

2️⃣ Install Dependencies
pip install opencv-python mediapipe pyautogui pygetwindow

3️⃣ Run the Project
python main.py


Make sure your webcam is connected and working.

✋ Gesture Mapping (Sample)
Gesture	Action
☝️ Index Finger	Move Mouse
✌️ Index + Middle	Left Click
🤟 Three Fingers	Right Click
👍 Thumb Up	Volume Up
✋ Four Fingers	Volume Down
✋ Open Palm	Play / Pause
👉 Swipe Right	Next (Media / Files)
👈 Swipe Left	Previous (Media / Files)
🎯 Use Cases

Touchless system interaction

Accessibility support

Smart media control

AI-based desktop automation

Hackathons & academic projects

👥 Team Members

Piyush Katoch

Divyansh Rana

Rahul Rana

Aaditya Sharma

📌 Future Enhancements

Custom gesture training

Mobile gesture control support

Voice + gesture hybrid control

ML-based gesture classification

GUI dashboard

📜 License

This project is open-source and free to use for educational purposes.
