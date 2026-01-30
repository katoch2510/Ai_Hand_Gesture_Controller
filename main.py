import cv2
import pyautogui
import pygetwindow as gw
from collections import deque

from hand_tracking import HandDetector
from gesture_recognition import Gesture
from mouse_control import MouseControl
from media_control import Media
from file_control import FileCtrl
from app_control import AppControl

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# ---------------- OBJECTS ----------------
hand = HandDetector()
gest = Gesture()
mouse = MouseControl()
media = Media()
files = FileCtrl()
apps = AppControl()

# ---------------- STATES ----------------
last_action = None
drag_active = False

# AI confidence history
gesture_history = deque(maxlen=5)

# Swipe detection
x_history = deque(maxlen=5)
swipe_cooldown = 0
SWIPE_THRESHOLD = 60
SWIPE_DELAY = 12

# 🔴 IMPORTANT: Volume NOT locked
lock_actions = {
    "LEFT_CLICK",
    "RIGHT_CLICK",
    "PLAY_PAUSE",
    "OPEN_YouTube",
    "OPEN_BROWSER",
    "VOL_UP",
    "VOL_DOWN"
}

screen_w, screen_h = pyautogui.size()

# ---------------- CONTEXT AWARE ----------------
def get_active_context():
    win = gw.getActiveWindow()
    if not win:
        return "UNKNOWN"

    title = win.title.lower()
    if "youtube" in title:
        return "YOUTUBE"
    elif "explorer" in title:
        return "FILES"
    elif "chrome" in title or "edge" in title:
        return "BROWSER"
    return "OTHER"


while True:
    success, img = cap.read()
    if not success:
        break

    img = hand.detect(img)
    lm = hand.landmarks(img)

    fingers = gest.fingers(lm)
    action = gest.get(fingers)
    context = get_active_context()

    confidence = 0.0

    if lm and action:
        cam_h, cam_w, _ = img.shape
        x, y = lm[8][1], lm[8][2]

        mapped_x = int(x * screen_w / cam_w)
        mapped_y = int(y * screen_h / cam_h)

        # -------- AI CONFIDENCE --------
        gesture_history.append(action)
        confidence = gesture_history.count(action) / len(gesture_history)

        if confidence < 0.7:
            action = None

        # -------- MOVE --------
        if action == "MOVE":
            mouse.move(mapped_x, mapped_y)
            last_action = None

        # -------- DRAG --------
        
        elif action == "DRAG":
            if not drag_active:
                mouse.drag_start()
                drag_active = True
            mouse.move(mapped_x, mapped_y)

        # -------- VOLUME (CONTINUOUS) --------
       # -------- VOLUME CONTROL (SMART) --------
        elif action == "VOL_UP":
            if context == "YOUTUBE":
                media.yt_vol_up()      # YouTube volume
            else:
                media.sys_vol_up()     # System volume
        elif action == "VOL_DOWN":
            if context == "YOUTUBE":
                media.yt_vol_down()    # YouTube volume
            else:
                media.sys_vol_down()   # System volume  

        # -------- LOCKED ACTIONS --------
        elif action in lock_actions and last_action != action:

            if action == "LEFT_CLICK":
                mouse.left_click()

            elif action == "RIGHT_CLICK":
                mouse.right_click()

            elif action == "PLAY_PAUSE":
                media.play_pause()

            elif action == "OPEN_YouTube":
                apps.open_youtube()

            elif action == "OPEN_BROWSER":
                apps.open_browser()

            last_action = action

        # -------- SWIPE --------
        x_history.append(x)

        if len(x_history) == x_history.maxlen and swipe_cooldown == 0:
            diff = x_history[-1] - x_history[0]

            if diff > SWIPE_THRESHOLD:
                if context == "YOUTUBE":
                    media.next()
                elif context == "FILES":
                    files.next()
                swipe_cooldown = SWIPE_DELAY
                x_history.clear()

            elif diff < -SWIPE_THRESHOLD:
                if context == "YOUTUBE":
                    media.previous()
                elif context == "FILES":
                    files.previous()
                swipe_cooldown = SWIPE_DELAY
                x_history.clear()

    else:
        if drag_active:
            mouse.drag_end()
            drag_active = False
        last_action = None
        gesture_history.clear()
        x_history.clear()

    if swipe_cooldown > 0:
        swipe_cooldown -= 1

    # -------- HUD --------
    cv2.putText(img, f"Gesture: {action}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(img, f"Confidence: {confidence*100:.0f}%", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.putText(img, f"Context: {context}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 255), 2)

    cv2.imshow("AI Gesture Control System", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
